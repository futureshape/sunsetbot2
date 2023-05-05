#!/bin/sh

# Temporarily interrupt video streaming to take a photo

sudo service youtube stop
raspistill -w 3280 -h 2464 -o /var/tmp/sunset.jpg
sudo service youtube start