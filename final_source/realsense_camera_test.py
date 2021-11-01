import pyrealsense2 as rs
import math
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
pipeline.start(config)
num_pics = 4
for x in range(0, num_pics):
	frames = pipeline.wait_for_frames()
        color = frames.get_color_frame()
        color_image = np.asanyarray(color.get_data())
	color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)
        cv2.imwrite('rs_image_' + str(x) + '.jpg', color_image)