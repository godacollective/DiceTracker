# Description
OpenCV based tracker of cubical dice, that response any number of dice and send array of values via OSC

### Arguments:

Select first video source, set lower threshold to 127 and upper to 255, turn on OSC sending, use localhost and port 5005:
```
    python dicetracker.py -v "0" -t "127 255" -s 1 -osc "127.0.0.1 5005"
```
  - [-v]: type number of video source or name of video file in root directory, default is "0"
  - [-t THRESHOLD] : specify lower and upper thresholds, default is "127 255"
  - [-s SEND] : if 0 OSC messaging is off, default is 1
  - [-osc]: specify IP address of the OSC server and port, that the OSC server is listening to, default is "127.0.0.1 5005"
  - [-m]: if 1 you'll see thresholded picture and printed values in consolas, default is 0
