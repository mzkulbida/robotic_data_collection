from niryo_one_python_api.niryo_one_api import *
import rospy
import math
import pyrealsense2 as rs
import cv2
import numpy as np

rospy.init_node('niryo_one_run_python_api_code')
n = NiryoOne()
PI = 3.1415
#object location(x,y,z)
center = (.3, 0, .085)
#distance in cm from robot position to object location
radius = .14
#the fact that the lens is not at the center of the camera must be accounted for
mag_offset = .033
#the amount of degrees panned by the camera between each image. lower value=more images
angle_diff = 5
#degrees between each vertical level
angle_diff_vert = 20
r_to_l = 1
acquire_imgs = True
q=0
#configures camera
if acquire_imgs:
	pipeline = rs.pipeline()
	config = rs.config()
	config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 15)
	pipeline.start(config)

for angle_deg_vert in range(0, 90, angle_diff_vert):
	angle_vert = angle_deg_vert * PI / 180
	z_pos = center[2] + math.sin(angle_vert) * radius
	pitch = angle_vert
	for angle_deg in range(-45, 45 + angle_diff, angle_diff):
		angle = angle_deg * PI / 180

		x_pos = center[0] - math.cos(angle) * math.cos(angle_vert) * radius
		y_pos = center[1] - math.sin(angle) * math.cos(angle_vert) * radius * r_to_l
		yaw = angle * r_to_l
		roll = 0
		
		x_copy = x_pos
		y_copy = y_pos

		x_pos = center[0] + r_to_l * math.sin(angle) * mag_offset - math.cos(angle) * math.cos(angle_vert) * radius
		y_pos = center[1] - math.cos(angle) * mag_offset - math.sin(angle) * math.cos(angle_vert) * radius * r_to_l
		try:
			
			n.move_pose(x_pos, y_pos, z_pos, roll, pitch, yaw)
			if acquire_imgs:
				n.wait(2)
				frames = pipeline.wait_for_frames()
				color = frames.get_color_frame()
				color_image = np.asanyarray(color.get_data())
				color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)
				cv2.imwrite('images2/' + 'img' + '{:03d}_{:.3f}_{:.3f}_{:.3f}_{:.3f}_{:.3f}_{:.3f}.jpg'.format(q, center[0]-x_copy, center[1]-y_copy, center[2]-z_pos, roll, pitch, yaw), color_image)
				q += 1
		except NiryoOneException:
			print( "Move to (", x_pos, ", ", y_pos, ", ", z_pos, ") failed")
	r_to_l *= -1