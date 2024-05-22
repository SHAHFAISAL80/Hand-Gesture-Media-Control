
# Hand Gesture Media Control

This project is a Python application that allows you to control media playback on your computer using hand gestures captured from a webcam.
By utilizing computer vision techniques with the Mediapipe library, the application detects and tracks the movement of your hand.
Based on the finger count and hand positions, it performs various media control actions.

## Features

- **Forward Skip**: Extend any one finger to skip forward .
- **Backward Skip**: Extend any two fingers to skip backward.
- **Volume Up**: Extend any three fingers to increase the volume.
- **Volume Down**: Extend any four fingers to decrease the volume.
- **Pause/Play**: Extend all five fingers to pause or resume playback.

## Requirements

- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI

## How to Use

1. Install the required dependencies mentioned.
2. Run the `project_media_control.py` script.
3. Position your hand in front of the webcam.
4. Perform the corresponding gesture to control media playback.

Please ensure that your webcam is properly configured and visible to the script.


## output


![Output Example](https://github.com/Anandukc/gesture_based_media_control/blob/master/example.mp4)
![Image 1](https://github.com/Anandukc/gesture_based_media_control/blob/master/hand1.png)
![Image 2](https://github.com/Anandukc/gesture_based_media_control/blob/master/hand2.png)
![Image 3](https://github.com/Anandukc/gesture_based_media_control/blob/master/hand3.png)

