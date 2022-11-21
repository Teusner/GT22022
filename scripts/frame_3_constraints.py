from manim import *
import numpy as np
from frame import Basis

# Scene config
config.media_dir = "./build/manim"
config.background_color = "#FAFAFA"
config.frame_height = 10
config.frame_width = 10

class frame_3_constraints(ThreeDScene):
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

        # Animation
        self.wait(0.5)

        self.begin_ambient_camera_rotation(rate=0.05)
        base_1.x.set_color(PURPLE)
        base_1.x_label.set_color(PURPLE)
        self.play(
            Rotate(base_1, -PI/4, axis=[1, 0, 0], about_point=[0, 0, 0]),
            run_time=0.5, rate_func=rate_functions.ease_out_bounce
        )
        self.wait(0.5)
        base_1.y.set_color(PURPLE)
        base_1.y_label.set_color(PURPLE)
        self.play(
            Rotate(base_1, -PI/4, axis=[0, 1, 0], about_point=[0, 0, 0]),
            run_time=0.5, rate_func=rate_functions.ease_out_bounce
        )
        self.remove(base_0.z, base_0.z_label)
        self.wait(0.5)
        base_1.z.set_color(PURPLE)
        base_1.z_label.set_color(PURPLE)
        self.play(
            Rotate(base_1, -PI/4, axis=[0, 0, 1], about_point=[0, 0, 0]),
            run_time=0.5, rate_func=rate_functions.ease_out_bounce
        )
        self.remove(base_0.x, base_0.x_label, base_0.y, base_0.y_label)
        self.wait(0.5)
        self.stop_ambient_camera_rotation()

        self.begin_ambient_camera_rotation(rate=-0.05)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        self.play(Unwrite(base_1), run_time=0.9)
        self.wait(0.1)