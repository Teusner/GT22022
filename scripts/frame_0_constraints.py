from manim import *
import numpy as np
from frame import Basis
from scipy.spatial.transform import Rotation


# Scene config
config.media_dir = "./build/manim"
config.background_color = "#FAFAFA"
config.frame_height = 10
config.frame_width = 10

class frame_0_constraints(ThreeDScene):
    def construct(self):
        base_0 = Basis()
        self.add_fixed_orientation_mobjects(*base_0.labels())

        # Animation
        self.set_camera_orientation(phi=45 * DEGREES, theta=45 * DEGREES, zoom=3)
        self.play(Write(base_0), run_time=1)

        # Base 1
        base_1 = Basis(id="1", x_color=RED, y_color=GREEN, z_color=BLUE)
        self.add_fixed_orientation_mobjects(*base_1.labels())
        self.play(Write(base_1), run_time=1)
        self.play(Rotate(base_1, angle=PI/4, axis=[0, 0, 1], about_point=[0, 0, 0]), run_time=0.33)
        self.play(Rotate(base_1, angle=PI/4, axis=[0, 1, 0], about_point=[0, 0, 0]), run_time=0.33)
        self.play(Rotate(base_1, angle=PI/4, axis=[1, 0, 0], about_point=[0, 0, 0]), run_time=0.33)
        R = Rotation.from_euler("zyx", [np.pi/4, np.pi/4, np.pi/4]).as_matrix()

        # Animation
        self.wait(0.5)

        self.begin_ambient_camera_rotation(rate=0.05)
        for i in range(3):
            self.play(Rotate(base_1, PI/3, axis=(R@np.eye(1, 3, i).T).flatten(), about_point=[0, 0, 0]), run_time=1, rate_func=rate_functions.there_and_back)
        self.stop_ambient_camera_rotation()

        self.begin_ambient_camera_rotation(rate=-0.05)
        self.play(Rotate(base_1, 2*PI, np.array([0, 0, 1]), about_point=[0, 0, 0]), run_time=3)
        self.stop_ambient_camera_rotation()

        self.play(Unwrite(base_0), Unwrite(base_1), run_time=0.9)
        self.wait(0.1)