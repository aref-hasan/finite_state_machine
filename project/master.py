from manim import *
import cv2
from manim_voiceover import VoiceoverScene
from manim.scene.moving_camera_scene import MovingCameraScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

class Main(MovingCameraScene):
    def construct(self):
        #self.greeting()
        #self.vid()
        #self.sound()
        self.dea_name()
        self.nea_title()
        self.nea_title_short()
        self.question_mark_animation()
        self.show_description()
        self.nea_title_short_up()
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


    def sound(self):
        self.play(Write(Text("Hello World!")), run_time=3)
        
        self.add_sound("../src/sounds/pokemon_original.mp3")

        self.play(FadeOut(Text("Hello World!")), run_time=1)


    def dea_name(self):
        text = Text("Deterministische endliche Automaten", font_size= 50)
        self.play(Write(text), run_time=3)
        self.wait(2)  
        self.play(FadeOut(text), run_time = 1)
        
    def nea_title(self):
        nea = Text("Nichtdeterministische endliche Automaten", font_size= 50)
        self.play(Write(nea), run_time=3)
        self.wait(1)  
        self.play(FadeOut(nea))

    def nea_title_short(self):
        self.nea = Text("NEA", font_size= 50)
        self.play(Write(self.nea))  
        self.wait(2)
        

    def question_mark_animation(self):
        question_mark = Text("?", font_size=50).next_to(self.nea, RIGHT)
        self.play(Write(question_mark))
        for _ in range(2): 
            self.play(question_mark.animate.scale(1.2), run_time=0.5)
            self.play(question_mark.animate.scale(0.8), run_time=0.5)
            self.play(question_mark.animate.scale(1.2), run_time=0.5)
            self.play(question_mark.animate.scale(0.001), run_time=0.9)

    def show_description(self):
        description = Text("= bei einer Eingabe, die Möglichkeit in mehrere Zustände zu wecheseln", font_size=25).next_to(self.nea, DOWN)
        self.play(Write(description))
        self.wait(6)
        self.clear()

    def nea_title_short_up(self):
        self.play(self.nea.animate.to_edge(UP))  # Move the title to left edge.
        self.wait(2)