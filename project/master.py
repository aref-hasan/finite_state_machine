
from manim import *
import cv2
from manim_voiceover import VoiceoverScene
from manim.scene.moving_camera_scene import MovingCameraScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService
###########################################################################
###########################################################################
###########################################################################

class Main(MovingCameraScene):
    def construct(self):
        self.greeting()
        self.welcome()
        self.pokemon_logo()
        self.vid()
        #self.sound()
        self.pokemon_fig()
        self.pokemon_components()
        self.pokemon_components_math()
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

    def welcome(self):
        welcome_text = Text("Herzlich willkommen zu unserem\nVideo über Zustandsautomaten!", 
                            font_size=48, 
                            color=WHITE)

        welcome_text.move_to(ORIGIN)
        self.wait(3)
        self.play(FadeOut(welcome_text))

    def pokemon_logo(self):
        self.image_logo = ImageMobject("../src/img/pokemon/pokemon_logo.png").scale(0.7)
        self.image_logo.move_to(ORIGIN)

        self.play(FadeIn(self.image_logo))
        self.wait(2)
        
        #self.play(ShrinkToCenter(self.image_logo))
    def vid(self):
        self.play(ShrinkToCenter(self.image_logo))
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

    def pokemon_fig(self):
        state2_img = ImageMobject("../src/img/pokemon/PNG/charmeleon.png").scale(1)
        state1_img = ImageMobject("../src/img/pokemon/PNG/charmander.png").scale(1).next_to(state2_img, LEFT, buff=2)
        state3_img = ImageMobject("../src/img/pokemon/PNG/charizard.png").scale(1).next_to(state2_img, RIGHT, buff=2)
        # transitions
        arrow1 = Arrow(start=state1_img.get_right(), end=state2_img.get_left(), buff=0.3)
        arrow2 = Arrow(start=state2_img.get_right(), end=state3_img.get_left(), buff=0.3)
        label1 = Text("Lvl 16").next_to(arrow1, UP, buff=0.1).scale(0.5)
        label2 = Text("Lvl 36").next_to(arrow2, UP, buff=0.1).scale(0.5)

        #  a white circle around state3_img
        circle_around_state3 = Circle(color=WHITE).scale(1.2)
        circle_around_state3.move_to(state3_img.get_center())

        # a diagonal arrow pointing to state1_img
        start_point = state1_img.get_center() + LEFT * 2 + UP * 1  # Adjust as needed
        diagonal_arrow = Arrow(start=start_point, end=state1_img.get_left(), buff=0.1)

        all_elements = Group(state1_img, state2_img, state3_img, arrow1, arrow2, label1, label2, circle_around_state3, diagonal_arrow)


        self.play(Create(diagonal_arrow))
        self.wait(3)
        self.play(FadeIn(state1_img))
        self.wait(3)
        self.play(Create(arrow1), Write(label1))
        self.wait(3)
        self.play(FadeIn(state2_img))
        self.wait(3)
        self.play(Create(arrow2), Write(label2))
        self.wait(3)
        self.play(FadeIn(state3_img))
        self.wait(3)
        self.play(Create(circle_around_state3))

         # Transform the entire group
        self.play(all_elements.animate.scale(0.6).to_edge(UP))

    def pokemon_components(self):
        self.components = VGroup(
            MathTex(r"Ein \text{ endlicher Automat ist ein 5-Tupel } (Q, \Sigma, \delta, q_0, F), \text{ wobei:}"),
            MathTex(r"Q \text{ ist eine endliche Menge von Zuständen;}"),
            MathTex(r"\Sigma \text{ ist das Eingabealphabet (eine endliche nicht-leere Menge von Symbolen);}"),
            MathTex(r"\delta \text{ ist die Zustandsübergangsfunktion: } Q \times \Sigma \rightarrow Q;"),
            MathTex(r"q_0 \text{ ist der Anfangszustand, ein Element von } Q;"),
            MathTex(r"F \text{ ist die Menge der Endzustände, eine Teilmenge von } Q.")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.components.scale(0.7)
        self.components.to_edge(LEFT, buff=0.75)
        self.play(LaggedStart(*[Write(comp) for comp in self.components], lag_ratio=0.9))  # Sequentially write the components with delay.
        self.wait(4)
        self.play(self.components.animate.scale(0.6).to_edge(LEFT, buff=0.3))
        self.surrounding_rectangle = SurroundingRectangle(self.components, buff=.1, color="white")
        self.play(Create(self.surrounding_rectangle))  
        self.wait(2)  

    def pokemon_components_math(self):
        ############################Line 1############################
        # Text parts of the expression
        text1 = MathTex("Q = \\{").scale(0.5)
        text2 = MathTex("\\}").scale(0.5)
        text3 = MathTex(",").scale(0.5)
        text4 = MathTex(",").scale(0.5)

        # Image objects (replace 'image_path' with the path to your images)
        image1 = ImageMobject("../src/img/pokemon/PNG/charmander.png").scale(0.2)
        image2 = ImageMobject("../src/img/pokemon/PNG/charmeleon.png").scale(0.2)
        image3 = ImageMobject("../src/img/pokemon/PNG/charizard.png").scale(0.2)

        # Positioning the objects
        text1.next_to(self.components[1], RIGHT)
        text1.to_edge(LEFT, buff=8) 
        image1.next_to(text1, RIGHT, buff=0.1)
        text3.next_to(image1, RIGHT, buff=0.1)
        image2.next_to(text3, RIGHT, buff=0.1)
        text4.next_to(image2, RIGHT, buff=0.1)
        image3.next_to(text4, RIGHT, buff=0.1)
        text2.next_to(image3, RIGHT, buff=0.1)

        # Add objects to the scene        
        self.add(text1, image1, text3, image2, text4, image3, text2)
        self.wait(4)

        ############################Line 2############################
        # Text parts of the expression
        text1 = MathTex("\Sigma = \\{").scale(0.5)
        text2 = MathTex("\\}").scale(0.5)
        text3 = MathTex(",").scale(0.5)
        
        # Image objects (replace 'image_path' with the path to your images)
        text16 = Text("Lvl 16").scale(0.3)
        text36 = Text("Lvl 36").scale(0.3)

        # Positioning the objects
        text1.next_to(self.components[2], RIGHT)
        text1.to_edge(LEFT, buff=8)
        text16.next_to(text1, RIGHT, buff=0.1)
        text3.next_to(text16, RIGHT, buff=0.1)
        text36.next_to(text3, RIGHT, buff=0.1)
        text2.next_to(text36, RIGHT, buff=0.1)

        # Add objects to the scene
        self.add(text1, text16, text3, text36, text2)
        self.wait(4)
        ############################Line 1############################
        # Text parts of the expression
        text1 = MathTex("\delta :").scale(0.5)
        text2 = MathTex(",").scale(0.5)
        text3 = MathTex("+").scale(0.5)
        text4 = MathTex(r"\rightarrow").scale(0.5)
        text5 = MathTex("+").scale(0.5)
        text6 = MathTex(r"\rightarrow").scale(0.5)

        # Image objects (replace 'image_path' with the path to your images)
        text16 = Text("Lvl 16").scale(0.3)
        text36 = Text("Lvl 36").scale(0.3)
        image1 = ImageMobject("../src/img/pokemon/PNG/charmander.png").scale(0.2)
        image2 = ImageMobject("../src/img/pokemon/PNG/charmeleon.png").scale(0.2)
        image2_2 = ImageMobject("../src/img/pokemon/PNG/charmeleon.png").scale(0.2)
        image3 = ImageMobject("../src/img/pokemon/PNG/charizard.png").scale(0.2)
        # Positioning the objects
        text1.next_to(self.components[3], RIGHT)
        text1.to_edge(LEFT, buff=8)
        image1.next_to(text1, RIGHT, buff=0.1)
        text3.next_to(image1, RIGHT, buff=0.1)
        text16.next_to(text3, RIGHT, buff=0.1)
        text4.next_to(text16, RIGHT, buff=0.1)
        image2.next_to(text4, RIGHT, buff=0.1)
        text2.next_to(image2, RIGHT, buff=0.1)
        image2_2.next_to(text2, RIGHT, buff=0.1)
        text5.next_to(image2_2, RIGHT, buff=0.1)
        text36.next_to(text5, RIGHT, buff=0.1)
        text6.next_to(text36, RIGHT, buff=0.1)
        image3.next_to(text6, RIGHT, buff=0.1)

        # Add objects to the scene
        self.add(text1, image1, text3, text16, text4, image2, text2, image2_2, text5, text36, text6, image3)
        self.wait(4)
        ############################Line 4############################
         # Text parts of the expression
        text1 = MathTex(r"q_0 = ").scale(0.5)
        text2 = MathTex(r"\in Q").scale(0.5)

        # Image objects (replace 'image_path' with the path to your images)
        image1 = ImageMobject("../src/img/pokemon/PNG/charmander.png").scale(0.2)

        # Positioning the objects
        text1.next_to(self.components[4], RIGHT)
        text1.to_edge(LEFT, buff=8)
        image1.next_to(text1, RIGHT, buff=0.1)
        text2.next_to(image1, RIGHT, buff=0.1)
    
        # Add objects to the scene
        self.add(text1, image1, text2)
        self.wait(4)
        ############################Line 5############################

        # Text parts of the expression
        text1 = MathTex(r"F = \{").scale(0.5)
        text2 = MathTex(r"\} \subseteq Q").scale(0.5)
        # Image objects (replace 'image_path' with the path to your images)
        image1 = ImageMobject("../src/img/pokemon/PNG/charizard.png").scale(0.2)

        # Positioning the objects
        text1.next_to(self.components[5], RIGHT)
        text1.to_edge(LEFT, buff=8)
        image1.next_to(text1, RIGHT, buff=0.1)
        text2.next_to(image1, RIGHT, buff=0.1)
    
        # Add objects to the scene
        self.add(text1, image1, text2)

        # Keep the scene displayed
        self.wait(4)

        self.clear()
        
###########################DEA###########################
        


###########################NEA###########################
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


    def sound(self):
        self.play(Write(Text("Hello World!")), run_time=3)
        
        self.add_sound("../src/sounds/pokemon_original.mp3")

        self.play(FadeOut(Text("Hello World!")), run_time=1)