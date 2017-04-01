#Description
OpenCV based tracker of cubical dice, that response any number of dice and send array of values via OSC

### Arguments:

Download latest 10 images with tag #test_tag every 10 seconds until 40 seconds have passed and send an OSC message with the filename):
```
    python dicetracker.py -t "127 255" -osc "127.0.0.1 5005"
```
  - [-t THRESHOLD] : specify lower and upper thresholds, default is "127 255"
  - [--osc]: specify IP address of the OSC server and port, that the OSC server is listening to, default is "127.0.0.1 5005"
