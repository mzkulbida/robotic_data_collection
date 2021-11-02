## Robotic Data Collection

- Objective: Proof of Concept
  - Using a robot arm mounted camera to automatically capture training data for a deep neural network
  - Each image collected is associated with a set of coordinates describing the pose(position: x,y,z, and orientation: roll, pitch, yaw) of the object(a toner cap in this example)
  - This was done using a Niryo One robotic arm and a RealSense d435 3D camera
  - Upon successfully being trained with this data, the neural network will return the pose of the camera relative to the object when fed a captured image

## Video of system in operation
![Picture of Robot](/images/Niryo1_high.gif)

What was required to achieve this:
- Writing a Python script to operate the camera and robot
- Designing and 3D printing a CAD model for an attachment piece to mount the camera to the arm
