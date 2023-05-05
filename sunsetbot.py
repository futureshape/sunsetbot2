from polybot import Bot
import sys, os

lat = "51.4847637N"
long = "0.0510414W"
offset = 5 # minutes before sunset

temp_capture_file = "/var/tmp/sunset.jpg"

class SunsetBot(Bot):
  def main(self):
    self.post(status="", imagefile=temp_capture_file)


# Set to False for production, otherwise it won't wait for the right amount of time
debug = True

sunwait_command = "/usr/local/bin/sunwait wait sunset {debug} {lat} {long} offset {offset}".format(debug = "debug" if debug else "", lat = lat, long = long, offset = offset)
print(sunwait_command)

sunwait_status = os.system(sunwait_command)
if sunwait_status != 0:
    print("sunwait returned error status, quitting")
    sys.exit()

if os.path.exists(temp_capture_file):
  os.remove(temp_capture_file)

take_photo_command = os.path.dirname(os.path.realpath(__file__)) + "/take-photo.sh"

os.system(take_photo_command)

if not os.path.exists(temp_capture_file):
    print("photo wasn't captured, quitting")
    sys.exit()

SunsetBot('sunsetbot').run()