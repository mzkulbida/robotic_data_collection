## Robotic Data Collection

- Objective: Proof of Concept
  - Using a robot arm mounted camera to automatically capture training data for a deep neural network
  - Each image collected is associated with a set of coordinates describing the pose(position: x,y,z, and orientation: roll, pitch, yaw) of the object(a toner cartridge in this example)
  - This was done using a Niryo One robotic arm and a RealSense d435 3d camera
  - When trained with this data, the neural network should return the position of the camera relative to the object when fed a captured image

## Video of system in operation
![Picture of Robot](/images/Niryo1_high.gif)

What was required to achieve this:
- Write a Python script to operate the camera and robot
- Design and 3d print a CAD model for an attachment piece between the camera and arm
