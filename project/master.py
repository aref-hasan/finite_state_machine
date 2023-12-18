from manim import *


class Main(MovingCameraScene):
    def construct(self):
        self.greeting()
        self.aktzeptoren()

    def greeting(self):
        text = Text("Hallo Zusammen!", font_size= 50)
        self.play(Write(text))
        self.wait(2)  
        self.clear()
