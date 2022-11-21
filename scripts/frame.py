from manim import *

class Basis(VGroup) :
    def __init__(self, *vmobjects, id="0", x_color=GRAY_D, y_color=GRAY_D, z_color=GRAY_D, **kwargs):
        super().__init__(*vmobjects, **kwargs)
        self.x = Arrow3D(start=[0, 0, 0], end=[1, 0, 0], resolution=8, color=x_color)
        self.y = Arrow3D(start=[0, 0, 0], end=[0, 1, 0], resolution=8, color=y_color)
        self.z = Arrow3D(start=[0, 0, 0], end=[0, 0, 1], resolution=8, color=z_color)
        self.x_label = Tex("$i_" + id + "$").set_color(x_color).move_to([1.25, 0, 0])
        self.y_label = Tex("$j_" + id + "$").set_color(y_color).move_to([0, 1.25, 0])
        self.z_label = Tex("$k_" + id + "$").set_color(z_color).move_to([0, 0, 1.25])
        self.add(self.x, self.y, self.z, self.x_label, self.y_label, self.z_label)

    def labels(self):
        return [self.x_label, self.y_label, self.z_label]