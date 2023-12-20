from manim import *
import cv2

class Main(MovingCameraScene):
    def construct(self):
        self.greeting()
        self.vid()
        
    def greeting(self):
        text = Text("Hallo Zusammen!", font_size= 50)
        self.play(Write(text))
        self.wait(2)  
        self.clear()

    def vid(self):
        cap = cv2.VideoCapture("../src/vid/pokeball_transition.mp4") #source: https://vfx.productioncrate.com/search/Pokeball+Transition+2&type=vfx
        flag = True
        while flag:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame)
                self.add(frame_img)
                self.wait(0.04)  # Anpassen für FPS
                self.remove(frame_img)
        cap.release()
