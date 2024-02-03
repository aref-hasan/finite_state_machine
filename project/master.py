from manim import *
import cv2
from manim_voiceover import VoiceoverScene
from manim.scene.moving_camera_scene import MovingCameraScene
from manim_voiceover.services.gtts import GTTSService

##############################################################################################################
################################################MAIN##########################################################
##############################################################################################################

class Main(MovingCameraScene, VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="de"))

        #self.greeting()
        #self.welcome()
        #self.pokemon_logo()
        #self.vid()
        #self.pokemon_fig()
        #self.pokemon_components()
        #self.pokemon_components_math()
        # DEA
        self.dea_graph()
        self.dea_table()
        self.dea_components()
        self.dea_titles()
        self.dea_example()
        # NEA
        self.nea_intro()
        self.nea_graph()
        self.nea_table()
        self.nea_components()
        self.nea_titles()
        self.nea_example()
        # DEA & NEA
        #self.dea_vs_nea()
        #self.aktzeptoren()

    def greeting(self):
        text = Text("Hallo Zusammen!", font_size= 50)
        with self.voiceover(text="Hallo Zusammen!") as tracker:
            self.play(Write(text), run_time=tracker.duration)
        self.wait(1)
        self.clear()

    def welcome(self):
        welcome_text = Text("Herzlich willkommen zu unserem\nVideo über Zustandsautomaten!", 
                            font_size=48, 
                            color=WHITE)

        welcome_text.move_to(ORIGIN)
        with self.voiceover(text="Herzlich willkommen zu unserem\nVideo über Zustandsautomaten!") as tracker1:
            self.play(Write(welcome_text), run_time=tracker1.duration)
        self.play(FadeOut(welcome_text))

    def pokemon_logo(self):
        self.image_logo = ImageMobject("../src/img/pokemon/pokemon_logo.png").scale(0.7)
        self.image_logo.move_to(ORIGIN)
        title_text = Text("Endliche Zustandsautomaten", 
                            font_size=48, 
                            color=WHITE)
        with self.voiceover(text="Heute tauchen wir in die faszinierende Welt der endlichen Zustandsautomaten ein. Diese Konzepte finden in der Informatik breite Anwendung, aber keine Sorge, wir machen es spannend und verständlich – mit Hilfe von Pokémon!") as tracker2:
            self.play(Write(title_text), run_time=tracker2.duration)
            self.play(FadeOut(title_text))

        with self.voiceover(text="Stellt euch einen endlichen Zustandsautomaten wie ein Spiel vor, in dem bestimmte Regeln gelten. Diese Regeln bestimmen, wie man von einem Zustand in einen anderen übergeht. Ähnlich wie in einem Pokémon-Spiel, wo ein Pokémon verschiedene Entwicklungsstufen durchläuft.") as tracker3:
            self.play(FadeIn(self.image_logo), run_time=tracker3.duration)
        self.wait(1)


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

        # Image 
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
        
        # Image 
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

        # Image 
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

        # Image 
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

        # Image
        image1 = ImageMobject("../src/img/pokemon/PNG/charizard.png").scale(0.2)

        # Positioning the objects
        text1.next_to(self.components[5], RIGHT)
        text1.to_edge(LEFT, buff=8)
        image1.next_to(text1, RIGHT, buff=0.1)
        text2.next_to(image1, RIGHT, buff=0.1)
    
        # Add objects to the scene
        self.add(text1, image1, text2)
        self.wait(4)

        self.clear()

#########################################################
###########################DEA###########################
#########################################################

    def dea_graph(self):

        self.dea_short = Text("DEA", font_size= 50)

        self.dea_long = Text("Deterministische endliche Automaten", font_size= 50)  

        # The 3 begining circles
        self.circle2 = Circle(radius=0.6, color=BLUE)
        self.circle2.move_to(ORIGIN)
        self.circle1 = Circle(radius=0.6, color=BLUE).next_to(self.circle2, LEFT, buff=2)
        self.circle3 = Circle(radius=0.6, color=BLUE).next_to(self.circle2, RIGHT, buff=2)
        
        # text inside the circles
        self.text1c = Text("1", font_size=24).move_to(self.circle1.get_center())
        self.text2c = Text("2", font_size=24).move_to(self.circle2.get_center())
        self.text3c = Text("3", font_size=24).move_to(self.circle3.get_center())

        # straight arrows
        arrow1 = Arrow(start=self.circle1.get_top() + DOWN * 0.4, end=self.circle2.get_top() + DOWN * 0.4, buff=0.7) 
        arrow2 = Arrow(start=self.circle2.get_top() + DOWN * 0.4, end=self.circle3.get_top() + DOWN * 0.4, buff=0.7)
        arrow3 = Arrow(start=self.circle2.get_bottom() + UP * 0.4, end=self.circle1.get_bottom() + UP * 0.4, buff=0.7)

        # straight arrow labels
        label1 = Text("a").next_to(arrow1, UP, buff=0.1).scale(0.5)
        label2 = Text("b").next_to(arrow2, UP, buff=0.1).scale(0.5)
        label3 = Text("a").next_to(arrow3, DOWN, buff=0.1).scale(0.5)

        # double circle for circle 3
        circle_around_state3 = Circle(color=BLUE).scale(0.5)
        circle_around_state3.move_to(self.circle3.get_center())

        # arrow for iniial state
        start_point = self.circle1.get_center() + LEFT * 2 + UP * 1 
        diagonal_arrow = Arrow(start=start_point, end=self.circle1.get_left(), buff=0.1)

        # coordinates for curved arrows
        radius = self.circle1.width / 1.5
        angle = 52 * DEGREES  
        start_x = radius * np.cos(angle)/ 1.6
        start_y = radius * np.sin(angle) 
        start_point_1 = self.circle1.get_center() + np.array([start_x, start_y, 5])
        start_point_3 = self.circle3.get_center() + np.array([start_x, start_y, 5])
        end_angle = angle + 45.5
        end_x = radius * np.cos(end_angle) / 1.6 
        end_y = radius * np.sin(end_angle)
        end_point_1 = self.circle1.get_center() + np.array([end_x, end_y, 2])
        end_point_3 = self.circle3.get_center() + np.array([end_x, end_y, 2])

        # curved arrows
        arrow_1 = CurvedArrow(start_point_1, end_point_1, color=WHITE, angle= 3)
        arrow_3 = CurvedArrow(start_point_3, end_point_3, color=WHITE, angle= 3)

        # curved arrow labels
        label_1 = Text("b", font_size=24, color=WHITE)
        label_3 = Text("a, b", font_size=24, color=WHITE)
        label_offset = np.array([0.2, 0.2, 0])
        label_1.move_to(arrow_1.point_from_proportion(0.5) + label_offset)
        label_3.move_to(arrow_3.point_from_proportion(0.5) + label_offset)


        self.dea_all_elements = Group(diagonal_arrow, self.circle1, self.text1c, arrow_1, label_1, arrow1, label1,
                                    arrow3, label3, self.circle2, self.text2c, arrow2, label2, self.circle3, self.text3c, arrow_3,
                                    label_3, circle_around_state3)

    

        
        ###################Scene Animations###################
        # DEA Title
        self.play(Write(self.dea_long), run_time=3)
        self.wait(2)  
        self.play(FadeOut(self.dea_long), run_time = 1)

        # DEA shortcut
        self.play(Write(self.dea_short))  
        self.wait(2)

        self.play(self.dea_short.animate.to_edge(UP)) 
        self.wait(2)

        # DEA Graph
        self.play(Create(diagonal_arrow))
        self.wait(3)
        self.play(FadeIn(self.circle1), Write(self.text1c))
        self.wait(3)
        self.play(Create(arrow_1), Write(label_1)) 
        self.wait(3)
        self.play(Create(arrow1), Write(label1))
        self.wait(3)
        self.play(Create(arrow3), Write(label3))
        self.wait(3)
        self.play(FadeIn(self.circle2), Write(self.text2c))  
        self.wait(3)
        self.play(Create(arrow2), Write(label2))
        self.wait(3)
        self.play(FadeIn(self.circle3), Write(self.text3c))
        self.wait(3)
        self.play(Create(arrow_3), Write(label_3))  
        self.wait(3)
        self.play(Create(circle_around_state3))
        
        self.wait(4)

        self.play(self.dea_all_elements.animate.next_to(self.dea_short, UP, buff = - 3.2).scale(0.6))

    def dea_table(self):

        custom_values = [
            [" ", "a", "b"],
            [1, 2, 1],
            [2, 1, 3],
            [3, 3, 3]
        ]
        string_values = [[str(item) for item in row] for row in custom_values]

        # Create a table with the custom values
        self.t1 = Table(
            string_values,
            include_outer_lines=True
        ).scale(0.7)

        # Color the first row and first column red
        
        self.t1.add_highlighted_cell((1, 2), color=RED)
        self.t1.add_highlighted_cell((1, 3), color=RED)
        self.t1.add_highlighted_cell((2, 1), color=RED)
        self.t1.add_highlighted_cell((3, 1), color=RED)
        self.t1.add_highlighted_cell((4, 1), color=RED)


        # Move the table to the left lower corner
        self.t1.to_corner(DOWN)

        # Adding text with an arrow
        text1 = Text("Zustand", font_size=36, color=WHITE)
        text1.next_to(self.t1.get_cell((2, 1)), LEFT, buff=1)
        arrow1 = Arrow(text1.get_right(), self.t1.get_cell((2, 1)).get_left(), buff=0.1)

        # Adding text with an arrow
        text2 = Text("Übergang", font_size=36, color=WHITE)
        text2.next_to(self.t1.get_cell((1, 3)), RIGHT, buff=1)
        arrow2 = Arrow(text2.get_left(), self.t1.get_cell((1, 3)).get_right(), buff=0.1)

        # Adding text with an arrow
        text3 = Text("resultierender Zustand", font_size=36, color=WHITE)
        text3.next_to(self.t1.get_cell((2, 3)), RIGHT, buff=1)
        arrow3 = Arrow(text3.get_left(), self.t1.get_cell((2, 3)).get_right(), buff=0.1)


        red_rectangle1 = Rectangle(color=RED).scale(0.3)
        red_rectangle1.surround(self.text1c)

        red_rectangle2 = Rectangle(color=RED).scale(0.3)
        red_rectangle2.surround(self.text1c)


        # table
        self.play(Create(self.t1))
        self.wait(2)
        self.add(text1, arrow1)
        self.wait(2)
        self.add(red_rectangle1)
        self.wait(2)
        self.remove(red_rectangle1)
        self.add(text2, arrow2)
        self.wait(2)
        self.add(red_rectangle2)
        self.wait(2)
        self.remove(red_rectangle2)
        self.add(text3, arrow3)
        self.wait(2)
        self.add(red_rectangle1)         
        self.wait(4)
        

        self.play(FadeOut(text1, arrow1, text2, arrow2, text3, arrow3, red_rectangle1))
        self.wait(2)

        self.play(self.t1.animate.to_edge(LEFT))
        self.wait(2)

    def dea_components(self):
        self.components = VGroup(
            MathTex("Q = \\{1, 2, 3\\}"),
            MathTex("\Sigma = \\{a, b\\}"),
            MathTex(r"\delta : 1 + a \rightarrow 2 ; 1 + b \rightarrow 1 ; 2 + a \rightarrow 1 ;"),
            MathTex(r"  2 + b \rightarrow 3 ; 3 + a \rightarrow 3 ; 3 + b \rightarrow 3"),
            MathTex(r"q_0 = 1 \in Q"),
            MathTex(r"F = \{3\} \subseteq Q")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.components.scale(0.7)
        self.components.next_to(self.t1.get_cell((2, 3)), RIGHT, buff=3.5)
        self.play(LaggedStart(*[Write(comp) for comp in self.components], lag_ratio=0.9))  # Sequentially write the components with delay.
        self.wait(2)  
        self.play(self.components.animate.scale(0.85).to_edge(RIGHT + DOWN, buff=1))
        self.surrounding_rectangle_components= SurroundingRectangle(self.components, buff=.1, color="white")
        self.play(Create(self.surrounding_rectangle_components)) 
        self.wait(4)
        
    def dea_titles(self):
        text_1 = Text("Übergangstabelle",font_size=36, color=WHITE).next_to(self.t1, UP)
        text_2 = Text("Bestandteile",font_size=36, color=WHITE).next_to(self.surrounding_rectangle_components, UP)
        text_3 = Text("Übergangsdiagramm",font_size=36, color=WHITE).next_to(text_1, UP, buff = 1)

        titles = Group(text_1,text_2, text_3)
        
        self.play(FadeIn(titles))
        
        self.play(FadeOut(titles, self.surrounding_rectangle_components, self.t1, self.components))
        
        self.wait(4)
        
    def dea_example(self):
        self.play(self.dea_all_elements.animate.move_to(ORIGIN + LEFT * 0.6))
        self.play(self.dea_all_elements.animate.scale(1/0.6))

        # add test sequence
        text_sequence = Text("Sequenz: a a b a b a", font_size=35).next_to(self.circle2, DOWN, buff=1)

        self.add(text_sequence)
        self.wait(4)

        question_mark = Text("?", font_size=50).next_to(text_sequence, RIGHT)
        self.play(Write(question_mark))
        for _ in range(2): 
            self.play(question_mark.animate.scale(1.2), run_time=0.5)
            self.play(question_mark.animate.scale(0.8), run_time=0.5)
            self.play(question_mark.animate.scale(1.2), run_time=0.5)
            self.play(question_mark.animate.scale(0.001), run_time=0.9)

        # go through the sequence in the Übergangstabelle
        rect_around_a1 = SurroundingRectangle(text_sequence[8], color=RED)
        rect_around_a2 = SurroundingRectangle(text_sequence[9], color=RED)
        rect_around_a3 = SurroundingRectangle(text_sequence[11], color=RED)
        rect_around_a4 = SurroundingRectangle(text_sequence[13], color=RED)
        rect_around_b1 = SurroundingRectangle(text_sequence[10], color=RED)
        rect_around_b2 = SurroundingRectangle(text_sequence[12], color=RED)
        rect_around_1 = SurroundingRectangle(self.text1c, color=RED)       
        rect_around_2 = SurroundingRectangle(self.text2c, color=RED)
        rect_around_3 = SurroundingRectangle(self.text3c, color=RED)


        arrow1_red = Arrow(start=self.circle1.get_top() + DOWN * 0.4, end=self.circle2.get_top() + DOWN * 0.4, buff=0.7, color=RED) 
        arrow2_red = Arrow(start=self.circle2.get_top() + DOWN * 0.4, end=self.circle3.get_top() + DOWN * 0.4, buff=0.7, color=RED)
        arrow3_red = Arrow(start=self.circle2.get_bottom() + UP * 0.4, end=self.circle1.get_bottom() + UP * 0.4, buff=0.7, color=RED)

        # coordinates for curved arrows
        radius = self.circle1.width / 1.5
        angle = 52 * DEGREES  
        start_x = radius * np.cos(angle)/ 1.6
        start_y = radius * np.sin(angle) 
        start_point_1 = self.circle1.get_center() + np.array([start_x, start_y, 5])
        start_point_3 = self.circle3.get_center() + np.array([start_x, start_y, 5])
        end_angle = angle + 45.5
        end_x = radius * np.cos(end_angle) / 1.6 
        end_y = radius * np.sin(end_angle)
        end_point_1 = self.circle1.get_center() + np.array([end_x, end_y, 2])
        end_point_3 = self.circle3.get_center() + np.array([end_x, end_y, 2])

        arrow4_red = CurvedArrow(start_point_1, end_point_1, color=RED, angle= 3)
        arrow5_red = CurvedArrow(start_point_3, end_point_3, color=RED, angle= 3)

        # 1. a in sequence
        self.add(rect_around_a1)
        self.wait(2)
        self.add(rect_around_1)
        self.wait(2)
        self.remove(rect_around_1)
        self.add(arrow1_red)
        self.wait(2)
        self.remove(arrow1_red)
        self.add(rect_around_2)
        self.wait(2)
        self.remove(rect_around_2)
        self.wait(1)
        self.remove(rect_around_a1)

        # 2. a in sequence
        self.add(rect_around_a2)
        self.wait(2)
        self.add(rect_around_2)
        self.wait(2)
        self.remove(rect_around_2)
        self.add(arrow3_red)
        self.wait(2)
        self.remove(arrow3_red)
        self.add(rect_around_1)
        self.wait(2)
        self.remove(rect_around_1)
        self.wait(1)
        self.remove(rect_around_a2)

        # 1. b in sequence
        self.add(rect_around_b1)
        self.wait(2)
        self.add(rect_around_1)
        self.wait(2)
        self.remove(rect_around_1)
        self.add(arrow4_red)
        self.wait(2)
        self.remove(arrow4_red)
        self.add(rect_around_1)
        self.wait(2)
        self.remove(rect_around_1)
        self.wait(1)
        self.remove(rect_around_b1)

        # 3. a in sequence
        self.add(rect_around_a3)
        self.wait(2)
        self.add(rect_around_1)
        self.wait(2)
        self.remove(rect_around_1)
        self.add(arrow1_red)
        self.wait(2)
        self.remove(arrow1_red)
        self.add(rect_around_2)
        self.wait(2)
        self.remove(rect_around_2)
        self.wait(1)
        self.remove(rect_around_a3)

        # 2. b in sequence
        self.add(rect_around_b2)
        self.wait(2)
        self.add(rect_around_2)
        self.wait(2)
        self.remove(rect_around_2)
        self.add(arrow2_red)
        self.wait(2)
        self.remove(arrow2_red)
        self.add(rect_around_3)
        self.wait(2)
        self.remove(rect_around_3)
        self.wait(1)
        self.remove(rect_around_b2)

        # 4. a in sequence
        self.add(rect_around_a4)
        self.wait(2)
        self.add(rect_around_3)
        self.wait(2)
        self.remove(rect_around_3)
        self.add(arrow5_red)
        self.wait(2)
        self.remove(arrow5_red)
        self.add(rect_around_3)
        self.wait(2)
        self.remove(rect_around_3)
        self.wait(1)
        self.remove(rect_around_a4)

        # add chekmark at the end of the sequence
        checkmark = Text("✓", font_size=50, color=GREEN).next_to(text_sequence, RIGHT)
        self.add(checkmark)
        self.wait(2)

        self.clear()

#########################################################
###########################NEA###########################
#########################################################
        
    def nea_intro(self):
        self.set_speech_service(GTTSService(lang="de"))

        # NEA title shortcut
        nea_long = Text("Nichtdeterministische endliche Automaten", font_size= 50)

        # NEA title shortcut
        self.nea = Text("NEA", font_size= 50)
        
        # question mark
        question_mark = Text("?", font_size=50).next_to(self.nea, RIGHT)

        # NEA description
        nea_description = Text("= bei einer Eingabe, die Möglichkeit in mehrere Zustände zu wecheseln", font_size=25).next_to(self.nea, DOWN)

        ###################Scene Animations###################
        # DEA title 
        with self.voiceover(text="Zunächst haben wir uns mit deterministischen endlichen Automaten befasst.") as tracker_dea_long:
            self.wait(3)
            self.play(Write(self.dea_long), run_time=tracker_dea_long.duration)
        self.play(FadeOut(self.dea_long), run_time = 1)

        # NEA title
        with self.voiceover(text="Jetzt wollen wir uns die andere Seite anschauen, nämlich die nichtdeterministischen endlichen Automaten") as tracker_nea_long:
            self.play(Write(nea_long), run_time=tracker_nea_long.duration)
        self.play(FadeOut(nea_long))

        # NEA title shortcut
        with self.voiceover(text="Kurzgesagt NEA") as tracker_nea:
            self.play(Write(self.nea), run_time=tracker_nea.duration)  
        self.wait(2)

        # question mark
        with self.voiceover(text="Aber was genau bedeutet NEA und worin unterscheiden sie sich von deterministischen endlichen Automaten") as tracker_question_mark:
            self.play(Write(question_mark),run_time=tracker_question_mark.duration)
            for _ in range(2): 
                self.play(question_mark.animate.scale(1.2), run_time=0.5)
                self.play(question_mark.animate.scale(0.8), run_time=0.5)
                self.play(question_mark.animate.scale(1.2), run_time=0.5)
                self.play(question_mark.animate.scale(0.001), run_time=0.9)

        # NEA description 
        with self.voiceover(text="Ähnlich wie ein D E A ist auch ein NEA ein endlicher Automat, der als Berechnungsmodell für formale Sprachen dient. Das bedeutet, dass wir auch hier, wie im Beispiel des DEA, berechnen können, ob ein Wort in der Sprache enthalten ist oder nicht. Im Gegensatz zu einem DEA arbeitet ein NEA nichtdeterministisch. Das bedeutet, dass bei einem NEA eine Eingabe zu mehreren verschiedenen Zuständen führen kann. Er hat also mehrere Möglichkeiten für den Folgezustand."):
            self.wait(22)
            self.play(Write(nea_description))
        self.wait(1)
        self.play(FadeOut(nea_description))
        self.wait()

        # move NEA shortcut up
        self.play(self.nea.animate.to_edge(UP))  
        self.wait(2)

    def nea_graph(self):
        self.set_speech_service(GTTSService(lang="de"))

        # The 3 begining circles
        self.nea_circle2 = Circle(radius=0.6, color=BLUE)
        self.nea_circle2.move_to(ORIGIN)
        self.nea_circle1 = Circle(radius=0.6, color=BLUE).next_to(self.nea_circle2, LEFT, buff=2)
        self.nea_circle3 = Circle(radius=0.6, color=BLUE).next_to(self.nea_circle2, RIGHT, buff=2)
        
        # text inside the circles
        self.nea_text1 = Text("1", font_size=24).move_to(self.nea_circle1.get_center())
        self.nea_text2 = Text("2", font_size=24).move_to(self.nea_circle2.get_center())
        self.nea_text3 = Text("3", font_size=24).move_to(self.nea_circle3.get_center())

        # straight arrows
        arrow1 = Arrow(start=self.nea_circle1.get_top() + DOWN * 0.4, end=self.nea_circle2.get_top() + DOWN * 0.4, buff=0.7) 
        arrow2 = Arrow(start=self.nea_circle2.get_top() + DOWN * 0.4, end=self.nea_circle3.get_top() + DOWN * 0.4, buff=0.7)
        arrow3 = Arrow(start=self.nea_circle2.get_bottom() + UP * 0.4, end=self.nea_circle1.get_bottom() + UP * 0.4, buff=0.7)

        # straight arrow labels
        label1 = Text("a").next_to(arrow1, UP, buff=0.1).scale(0.5)
        label2 = Text("b").next_to(arrow2, UP, buff=0.1).scale(0.5)
        label3 = Text("a").next_to(arrow3, DOWN, buff=0.1).scale(0.5)

        # double circle for circle 3
        circle_around_state3 = Circle(color=BLUE).scale(0.5)
        circle_around_state3.move_to(self.nea_circle3.get_center())

        # arrow for iniial state
        start_point = self.nea_circle1.get_center() + LEFT * 2 + UP * 1 
        diagonal_arrow = Arrow(start=start_point, end=self.nea_circle1.get_left(), buff=0.1)

        # coordinates for curved arrows
        radius = self.nea_circle1.width / 1.5
        angle = 52 * DEGREES  
        start_x = radius * np.cos(angle)/ 1.6
        start_y = radius * np.sin(angle) 
        start_point_1 = self.nea_circle1.get_center() + np.array([start_x, start_y, 5])
        start_point_3 = self.nea_circle3.get_center() + np.array([start_x, start_y, 5])
        end_angle = angle + 45.5
        end_x = radius * np.cos(end_angle) / 1.6 
        end_y = radius * np.sin(end_angle)
        end_point_1 = self.nea_circle1.get_center() + np.array([end_x, end_y, 2])
        end_point_3 = self.nea_circle3.get_center() + np.array([end_x, end_y, 2])

        # curved arrows
        arrow_1 = CurvedArrow(start_point_1, end_point_1, color=WHITE, angle= 3)
        arrow_3 = CurvedArrow(start_point_3, end_point_3, color=WHITE, angle= 3)

        # curved arrow labels
        self.label_1 = Text("a, b", font_size=24, color=WHITE)
        label_3 = Text("a, b", font_size=24, color=WHITE)
        label_offset = np.array([0.2, 0.2, 0])
        self.label_1.move_to(arrow_1.point_from_proportion(0.5) + label_offset)
        label_3.move_to(arrow_3.point_from_proportion(0.5) + label_offset)
        
        # red rectangles
        self.red_surrounding_rectangle = SurroundingRectangle(self.label_1, buff=.1, color="red")
        self.red_surrounding_rectangle_a = SurroundingRectangle(label1, buff=.1, color="red")

        # all nea graph elements (without the red rectangles)
        self.nea_graph_elements = Group(diagonal_arrow, self.nea_circle1, self.nea_text1, arrow_1, self.label_1, arrow1,
                            label1, arrow3, label3, self.nea_circle2, self.nea_text2, arrow2, label2,
                            self.nea_circle3, self.nea_text3, arrow_3, label_3, circle_around_state3)
        
        # all nea graph elements (with the red rectangles)
        self.nea_all_elements = Group(diagonal_arrow, self.nea_circle1, self.nea_text1, arrow_1, self.label_1, arrow1,
                            label1, arrow3, label3, self.nea_circle2, self.nea_text2, arrow2, label2,
                            self.nea_circle3, self.nea_text3, arrow_3, label_3, circle_around_state3,
                            self.red_surrounding_rectangle, self.red_surrounding_rectangle_a)
        
        # NEA right side
        nea_graph_animation = self.nea_all_elements.animate.scale(0.6).to_edge(RIGHT, buff=0.5)
        nea_title_animation = self.nea.animate.scale(0.7).to_edge(RIGHT, buff=2.8)

        # DEA
        dea_title_shortcut = Text("DEA", font_size=50).scale(0.7).to_edge(UP).to_edge(LEFT, buff=2.8)
        dea_graph = self.dea_all_elements.to_edge(LEFT, buff=0.5)


        ###################Scene Animations###################
        # # the create of NEA graph
        # self.play(Create(diagonal_arrow))
        # self.wait(3)
        # self.play(FadeIn(self.nea_circle1), Write(self.nea_text1))
        # self.wait(3)
        # self.play(Create(arrow_1), Write(self.label_1)) 
        # self.wait(3)
        # self.play(Create(arrow1), Write(label1))
        # self.wait(3)
        # self.play(Create(arrow3), Write(label3))
        # self.wait(3)
        # self.play(FadeIn(self.nea_circle2), Write(self.nea_text2))  
        # self.wait(3)
        # self.play(Create(arrow2), Write(label2))
        # self.wait(3)
        # self.play(FadeIn(self.nea_circle3), Write(self.nea_text3))
        # self.wait(3)
        # self.play(Create(arrow_3), Write(label_3))  
        # self.wait(3)
        # self.play(Create(circle_around_state3))
        # self.wait(5)
        with self.voiceover(text="Nehmen wir als Beispiel den Anfangszustand"):
            self.wait(2)
            self.play(FadeIn(self.nea_graph_elements))
            self.wait(3)

        #red rectangle (a,b)
        with self.voiceover(text="Bei der Eingabe 'a' kann der Automat entweder in Zustand 1 verbleiben oder zum Zustand 2 wechseln"):
            self.wait(2)
            self.play(Create(self.red_surrounding_rectangle))
            self.wait(1)
        #red rectangle (a)
            self.play(Create(self.red_surrounding_rectangle_a))  
            self.wait(3)

        # move NEA
        nea_animations = AnimationGroup(nea_graph_animation,nea_title_animation)
        self.play(nea_animations)

        with self.voiceover(text="Wenn Wir den NEA Graph mit der Vorherigen D E A graph vergleichen sehen wir, dass bei den D E A Graphen bei der Eingabe 'a' nur eine Möglichkeit für den Folgezustand, nämlich Zustand 2."):
        # show DEA 
        # DEA title
            self.play(FadeIn(dea_title_shortcut, shift=DOWN))
        # DEA graph
            dea_graph.next_to(dea_title_shortcut, DOWN, buff =0.4)
            self.play(FadeIn(dea_graph, scale=0.1))
            self.wait(8)  
        
        # Fadeout DEA 
        self.play(FadeOut(dea_graph,dea_title_shortcut))
        self.wait(1)

        # move NEA title back
        nea_title_animation = self.nea.animate.move_to(UP * 3.5)  
        self.play(nea_title_animation)
        
        # move NEA graph back
        self.nea_all_elements.remove(self.red_surrounding_rectangle, self.red_surrounding_rectangle_a)
        self.nea_all_elements.next_to(self.nea, UP, buff= - 2.4)

        #nea_graph_animation = self.nea_all_elements.animate.next_to(self.nea, UP, buff= - 2.4)
        #self.red_surrounding_rectangle_animation = FadeOut(self.red_surrounding_rectangle)
        #self.red_surrounding_rectangle_a_animation = FadeOut(self.red_surrounding_rectangle_a)

        #Group all animation
        #self.nea_animations = AnimationGroup(self.red_surrounding_rectangle_animation, self.red_surrounding_rectangle_a_animation, nea_graph_animation)

        #self.play(self.nea_animations)
        self.wait(4)

    def nea_table(self):

        custom_values = [
            [" ", "a", "b"],
            [1, "{1,2}", 1],
            [2, 1, 3],
            [3, 3, 3]
        ]
        string_values = [[str(item) for item in row] for row in custom_values]

        # Create a table with the custom values
        self.nea_t1 = Table(
            string_values,
            include_outer_lines=True
        ).scale(0.7)

        # Color the first row and first column red
        
        self.nea_t1.add_highlighted_cell((1, 2), color=RED)
        self.nea_t1.add_highlighted_cell((1, 3), color=RED)
        self.nea_t1.add_highlighted_cell((2, 1), color=RED)
        self.nea_t1.add_highlighted_cell((3, 1), color=RED)
        self.nea_t1.add_highlighted_cell((4, 1), color=RED)


        # Move the table to the left lower corner
        self.nea_t1.to_corner(DOWN)

        # Adding text with an arrow
        nea_t1_text1 = Text("Zustand", font_size=36, color=WHITE)
        nea_t1_text1.next_to(self.nea_t1.get_cell((2, 1)), LEFT, buff=1)
        arrow1 = Arrow(nea_t1_text1.get_right(), self.nea_t1.get_cell((2, 1)).get_left(), buff=0.1)

        # Adding text with an arrow
        self.nea_t1_text2 = Text("Übergang", font_size=36, color=WHITE)
        self.nea_t1_text2.next_to(self.nea_t1.get_cell((1, 3)), RIGHT, buff=1)
        arrow2 = Arrow(self.nea_t1_text2.get_left(), self.nea_t1.get_cell((1, 3)).get_right(), buff=0.1)

        # Adding text with an arrow
        self.nea_t1_text3 = Text("resultierender Zustand", font_size=36, color=WHITE)
        self.nea_t1_text3.next_to(self.nea_t1.get_cell((2, 3)), RIGHT, buff=1)
        arrow3 = Arrow(self.nea_t1_text3.get_left(), self.nea_t1.get_cell((2, 3)).get_right(), buff=0.1)


        red_rectangle1 = Rectangle(color=RED).scale(0.3)
        red_rectangle1.surround(self.nea_text1)

        red_rectangle2 = Rectangle(color=RED).scale(0.3)
        red_rectangle2.surround(self.label_1)

        ###################Scene Animations###################

        # table
        with self.voiceover(text="Wenn wir uns die Zustandstabelle des NEA anschauen, wird der Unterschied deutlicher."):
            self.play(Create(self.nea_t1))
            self.wait(5)
            with self.voiceover(text="Zustand 1 sieht man, dass bei der Eingabe 'a' zwei mögliche Folgezustände existieren: entweder bleibt der Automat im Zustand 1 oder wechselt zum Zustand 2. Alle anderen Übergänge bleiben unverändert, da der Graph nur an dieser Stelle geändert wurde."):
                self.add(nea_t1_text1, arrow1)
                self.wait(2)
                self.add(red_rectangle1)
                self.wait(2)
                self.remove(red_rectangle1)
                self.add(self.nea_t1_text2, arrow2)
                self.wait(2)
                self.add(red_rectangle2)
                self.wait(2)
                self.remove(red_rectangle2)
                self.add(self.nea_t1_text3, arrow3)
                self.wait(2)
                self.add(red_rectangle1)         
                self.wait(10)
                self.play(FadeOut(nea_t1_text1, arrow1, self.nea_t1_text2, arrow2, self.nea_t1_text3, arrow3, red_rectangle1))
                self.wait(1)

            self.play(self.nea_t1.animate.to_edge(LEFT))
            self.wait(2)

    def nea_components(self):
        self.components_text= VGroup(
            MathTex("Q = \\{1, 2, 3\\}"),
            MathTex("\Sigma = \\{a, b\\}"),
            MathTex(r"\delta :1 + a \rightarrow 1; 1 + a \rightarrow 2 ; 1 + b \rightarrow 1 ; 2 + a \rightarrow 1 ;"),
            MathTex(r"  2 + b \rightarrow 3 ; 3 + a \rightarrow 3 ; 3 + b \rightarrow 3"),
            MathTex(r"q_0 = 1 \in Q"),
            MathTex(r"F = \{3\} \subseteq Q")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.components_text.scale(0.7)
        self.components_text.next_to(self.t1.get_cell((2, 3)), RIGHT, buff=3.5)

        


        ###################Scene Animations###################
        # components
        with self.voiceover(text="Hinsichtlich der Bestandteile des NEA sind diese im Beispiel ähnlich wie beim D E A."):

            self.play(LaggedStart(*[Write(comp) for comp in self.components_text], lag_ratio=0.9))  # Sequentially write the components with delay.
            self.wait(2)  
            self.play(self.components_text.animate.scale(0.85).to_edge(RIGHT + DOWN, buff=1))
            self.wait(1)  

        with self.voiceover(text="Der einzige Unterschied ist, dass die Zustandsübergangsfunktionen im ersten Zustand bei der Eingabe 'a' zwei verschiedene Folgezustände ermöglichen."):
            # rectangle
            self.surrounding_rectangle_components_nea= SurroundingRectangle(self.components_text, buff=.1, color="white")
            self.play(Create(self.surrounding_rectangle_components_nea)) 
            self.wait(4)

    def nea_titles(self):
        text_1 = Text("Übergangstabelle",font_size=36, color=WHITE).next_to(self.nea_t1, UP)
        text_2 = Text("Bestandteile",font_size=36, color=WHITE).next_to(self.surrounding_rectangle_components_nea, UP)
        text_3 = Text("Übergangsdiagramm",font_size=36, color=WHITE).next_to(text_1, UP, buff = 1)

        titles = Group(text_1,text_2, text_3)
       
        self.play(FadeIn(titles))
        self.wait(3)
        ###################Scene Animations###################
        with self.voiceover(text="Lass uns mal den NEA anhand eines Beispiels besser verstehen."):
            self.play(FadeOut(titles, self.surrounding_rectangle_components_nea, self.nea_t1, self.components_text))
            self.wait(2)
    
    def nea_example(self):
        # move nea graph down
        self.play(self.nea_all_elements.animate.move_to(ORIGIN + LEFT * 0.5))
        self.play(self.nea_all_elements.animate.scale(1/0.6))
        self.wait(2)



        # add test sequence
        text_sequence = Text("Sequenz: a a b a b a", font_size=35).next_to(self.nea_circle2, DOWN, buff=1)
        
        #question mark
        question_mark = Text("?", font_size=50).next_to(text_sequence, RIGHT)

        
        ###################Scene Animations###################
        
        # add the example
        with self.voiceover(text="Wir verwenden die gleiche Sequenz wie beim 'D E A': 'a',,,, 'a',,,,, 'b',,,, 'a',,,, 'b',,,, 'a'. Die Frage ist, wie der resultierende Zustand aussieht."):

            self.play(Write(text_sequence))
            self.wait(7)

            self.play(Write(question_mark))
            for _ in range(2): 
                self.play(question_mark.animate.scale(1.2), run_time=0.5)
                self.play(question_mark.animate.scale(0.8), run_time=0.5)
                self.play(question_mark.animate.scale(1.2), run_time=0.5)
                self.play(question_mark.animate.scale(0.001), run_time=0.9)

        # go through the sequence in the Übergangstabelle
        rect_around_a1 = SurroundingRectangle(text_sequence[8], color=RED)
        rect_around_a2 = SurroundingRectangle(text_sequence[9], color=RED)
        rect_around_a3 = SurroundingRectangle(text_sequence[11], color=RED)
        rect_around_a4 = SurroundingRectangle(text_sequence[13], color=RED)
        rect_around_b1 = SurroundingRectangle(text_sequence[10], color=RED)
        rect_around_b2 = SurroundingRectangle(text_sequence[12], color=RED)
        rect_around_1 = SurroundingRectangle(self.nea_circle1, color=RED)       
        rect_around_2 = SurroundingRectangle(self.nea_circle2, color=RED)
        rect_around_3 = SurroundingRectangle(self.nea_circle3, color=RED)
        #arrows
        arrow1_red = Arrow(start=self.nea_circle1.get_top() + DOWN * 0.4, end=self.nea_circle2.get_top() + DOWN * 0.4, buff=0.7, color=RED)
        arrow2_red = Arrow(start=self.nea_circle2.get_top() + DOWN * 0.4, end=self.nea_circle3.get_top() + DOWN * 0.4, buff=0.7, color=RED)
        arrow3_red = Arrow(start=self.nea_circle2.get_bottom() + UP * 0.4, end=self.nea_circle1.get_bottom() + UP * 0.4, buff=0.7, color=RED)
       

       # coordinates for curved arrows
        radius = self.nea_circle1.width / 1.5
        angle = 52 * DEGREES  
        start_x = radius * np.cos(angle)/ 1.6
        start_y = radius * np.sin(angle) 
        start_point_1 = self.nea_circle1.get_center() + np.array([start_x, start_y, 5])
        start_point_3 = self.nea_circle3.get_center() + np.array([start_x, start_y, 5])
        end_angle = angle + 45.5
        end_x = radius * np.cos(end_angle) / 1.6 
        end_y = radius * np.sin(end_angle)
        end_point_1 = self.nea_circle1.get_center() + np.array([end_x, end_y, 2])
        end_point_3 = self.nea_circle3.get_center() + np.array([end_x, end_y, 2])

        arrow4_red = CurvedArrow(start_point_1, end_point_1, color=RED, angle= 3)
        arrow4_green = CurvedArrow(start_point_1, end_point_1, color=GREEN, angle= 3)

        arrow5_red = CurvedArrow(start_point_3, end_point_3, color=RED, angle= 3)

        results_data_1 = [["-> 1", "2", "1", "1", "2", "3", "3"]]
        nea_results_table = Table(results_data_1, include_outer_lines=True).scale(0.4)
        nea_results_table.next_to(text_sequence, DOWN, buff=0.35)
        

        # crate nea results table
        self.add(rect_around_1)
        self.wait(2)
        element = nea_results_table.get_entries((1, 1))
        self.play(FadeIn(element))
        self.wait(1)

        # 1. a in sequence
        with self.voiceover(text="""Unser Anfangszustand ist '1'. Bei der ersten Eingabe 'a' hat man zwei Möglichkeiten:
                                 Entweder wechselt man zum Zustand 2 oder bleibt im Zustand 1. Wir betrachten beide Optionen.
                                 Wählen wir zuerst den Übergang zum Zustand 2. Bei der zweiten Eingabe 'a' kehren wir zum Zustand 1 zurück.
                                 Bei der dritten Eingabe 'b' bleiben wir im Zustand 1. """):
            self.add(rect_around_a1)
            self.wait(4)
            self.add(arrow1_red)
            self.wait(3)
            self.add(arrow4_green)
            self.wait(3)
            self.remove(arrow4_green)
            self.remove(arrow1_red)
            self.wait(2)
            self.add(arrow1_red)
            self.wait(0.5)
            self.add(rect_around_2)
            self.wait(1)
            element2 = nea_results_table.get_entries((1, 2))
            self.play(FadeIn(element2))        
            self.wait(1)
            self.remove(rect_around_a1)
        # 2. a in sequence
            self.add(rect_around_a2)
            self.wait(1)
            self.remove(rect_around_2)
            self.wait(0.5)
            self.add(rect_around_2)
            self.wait(2)
            element3 = nea_results_table.get_entries((1, 3))
            self.play(FadeIn(element3))      
            self.add(arrow3_red)
            self.wait(2)
            self.remove(rect_around_1)
            self.add(rect_around_1)
            self.wait(2)
            self.remove(rect_around_a2)
        # 1. b in sequence
            self.add(rect_around_b1)
            self.wait(1)
            self.add(arrow4_red)
            self.wait(1)
            self.remove(rect_around_1)
            self.wait(0.5)
            self.add(rect_around_1)
            element4 = nea_results_table.get_entries((1, 4))
            self.play(FadeIn(element4))  
            self.wait(1)
            self.remove(rect_around_b1)

        # 3. a in sequence
        with self.voiceover(text="""Die vierte Eingabe ist 'a', wo wir wieder zwei Optionen haben.
                             Wir bleiben jedoch bei unserer Option und wechseln zum Zustand 2"""):
            self.add(rect_around_a3)
            self.wait(1)
            self.remove(0.5)
            self.add(arrow1_red)
            self.wait(1)
            self.add(arrow4_green)
            self.wait(1)
            self.remove(arrow4_green)
            self.remove(arrow1_red)
            self.wait(1)
            self.add(arrow1_red)
            self.wait(2)
            self.remove(rect_around_2)
            self.wait(0.5)
            self.add(rect_around_2)
            self.wait(2)
            element5 = nea_results_table.get_entries((1, 5))
            self.play(FadeIn(element5))  
            self.remove(rect_around_a3)

        # 2. b in sequence
        with self.voiceover(text="""Bei der fünften Eingabe 'b' erreichen wir den Endzustand 3,
                                 und alle weiteren Eingaben führen ebenfalls zu diesem Zustand."""):

            self.add(rect_around_b2)
            self.wait(2)
            self.add(arrow2_red)
            self.wait(2)
            self.add(rect_around_3)
            element6 = nea_results_table.get_entries((1, 6))
            self.play(FadeIn(element6))
            self.wait(2)
            self.remove(rect_around_b2)

            # 4. a in sequence
            self.add(rect_around_a4)
            self.wait(1)
            self.add(arrow5_red)
            self.wait(1)
            self.remove(rect_around_3)
            self.wait(0.5)
            self.add(rect_around_3)
            self.wait(1)
            element7= nea_results_table.get_entries((1, 7))
            self.play(FadeIn(element7))
            self.wait(2)
            self.remove(rect_around_a4)

        with self.voiceover(text="Somit haben wir die Sequenz abgearbeitet und können einen Check eintragen!"):
            # add chekmark at the end of the sequence
            checkmark = Text("✓", font_size=50, color=GREEN).next_to(text_sequence, RIGHT)
            self.wait(2)
            self.add(checkmark)
            self.wait(3)
            self.remove(rect_around_a1,rect_around_a2,rect_around_a3,rect_around_a4, rect_around_b1,
                        rect_around_b2, rect_around_1, rect_around_2, rect_around_3, arrow1_red, 
                        arrow2_red, arrow3_red, arrow4_red, arrow5_red, nea_results_table, checkmark,
                        element, element2, element3, element4, element5, element6, element7)
            self.wait(2) 

        ################################################################
        # go through the sequence in the Übergangstabelle
        rect_around_a1_green = SurroundingRectangle(text_sequence[8], color=GREEN)
        rect_around_a2_green = SurroundingRectangle(text_sequence[9], color=GREEN)
        rect_around_a3_green = SurroundingRectangle(text_sequence[11], color=GREEN)
        rect_around_a4_green = SurroundingRectangle(text_sequence[13], color=GREEN)
        rect_around_b1_green = SurroundingRectangle(text_sequence[10], color=GREEN)
        rect_around_b2_green = SurroundingRectangle(text_sequence[12], color=GREEN)
        rect_around_1_green = SurroundingRectangle(self.nea_circle1, color=GREEN)       
        rect_around_2_green = SurroundingRectangle(self.nea_circle2, color=GREEN)
        rect_around_3_green = SurroundingRectangle(self.nea_circle3, color=GREEN)

        #arrows
        arrow1_green = Arrow(start=self.nea_circle1.get_top() + DOWN * 0.4, end=self.nea_circle2.get_top() + DOWN * 0.4, buff=0.7, color=GREEN)
        arrow2_green = Arrow(start=self.nea_circle2.get_top() + DOWN * 0.4, end=self.nea_circle3.get_top() + DOWN * 0.4, buff=0.7, color=GREEN)
        arrow3_green = Arrow(start=self.nea_circle2.get_bottom() + UP * 0.4, end=self.nea_circle1.get_bottom() + UP * 0.4, buff=0.7, color=GREEN)
       

       # coordinates for curved arrows
        radius = self.nea_circle1.width / 1.5
        angle = 52 * DEGREES  
        start_x = radius * np.cos(angle)/ 1.6
        start_y = radius * np.sin(angle) 
        start_point_1 = self.nea_circle1.get_center() + np.array([start_x, start_y, 5])
        start_point_3 = self.nea_circle3.get_center() + np.array([start_x, start_y, 5])
        end_angle = angle + 45.5
        end_x = radius * np.cos(end_angle) / 1.6 
        end_y = radius * np.sin(end_angle)
        end_point_1 = self.nea_circle1.get_center() + np.array([end_x, end_y, 2])
        end_point_3 = self.nea_circle3.get_center() + np.array([end_x, end_y, 2])

        arrow4_green = CurvedArrow(start_point_1, end_point_1, color=GREEN, angle= 3)

        arrow5_green = CurvedArrow(start_point_3, end_point_3, color=GREEN, angle= 3)
       
        results_data_2 = [["-> 1", "1", "2", "3", "3", "3", "3"]]
        nea_results_table_2 = Table(results_data_2, include_outer_lines=True).scale(0.4)
        nea_results_table_2.next_to(text_sequence, DOWN, buff=0.35)

        # crate nea results table
        self.add(rect_around_1_green)
        self.wait(5)  
        element1 = nea_results_table_2.get_entries((1, 1))

        with self.voiceover(text="""Lass uns nun die gleiche Sequenz durchgehen, aber dieses Mal wählen wir die
                                andere Option für den Übergang des Folgezustandes. Unser Anfangszustand bleibt der gleiche, also „1“ """):
            self.play(FadeIn(element1))
            self.wait(1)

        # 1. a in sequence
        with self.voiceover(text="""Bei der ersten Eingabe „a“ haben wir, wie schon erwähnt, zwei verschiedene Übergangsmöglichkeiten.
                                Da wir im ersten Durchlauf den Folgezustand „2“ ausgewählt haben, nehmen wir hier den anderen Übergang, 
                                also bleiben wir im Zustand „1“."""):
            self.wait(3)
            self.add(rect_around_a1_green)
            self.wait(2)
            self.add(arrow1_green)
            self.wait(1)
            self.add(arrow4_green)
            self.wait(1)
            self.remove(arrow4_green)
            self.remove(arrow1_green)
            self.wait(1)
            self.add(arrow4_green)
            self.wait(2)
            self.remove(rect_around_1_green)
            self.wait(1)
            self.add(rect_around_1_green)
            self.wait(2)
            element2 = nea_results_table_2.get_entries((1, 2))
            self.play(FadeIn(element2))        
            self.wait(3)
            self.remove(rect_around_a1_green)

        # 2. a in sequence
        with self.voiceover(text="""Bei der zweiten Eingabe „a“ stehen uns erneut zwei Möglichkeiten zur Verfügung:
                                 entweder im Zustand „1“ zu verbleiben oder zum Zustand „2“ zu wechseln.  Wir entscheiden
                                 uns für die zweite Option und wechseln zum Zustand „2“."""):
            self.add(rect_around_a2_green)
            self.wait(2)
            self.remove(arrow4_green)
            self.wait(1)
            self.add(arrow4_green)
            self.wait(2)
            self.add(arrow1_green)
            self.wait(1)
            self.add(rect_around_2_green)
            element3 = nea_results_table_2.get_entries((1, 3))
            self.play(FadeIn(element3))      
            self.wait(2)
            self.remove(rect_around_a2_green)

        # 1. b in sequence
        with self.voiceover(text=" Bei der dritten Eingabe, also „b“, haben wir nur eine Übergangsmöglichkeit und wechseln zum Zustand „3“, welcher unser Endzustand ist. Wie bereits erwähnt, führen in diesem Beispiel, nachdem der Endzustand erreicht wurde, alle weiteren Eingaben zum gleichen Endzustand als Folgezustand."):

            self.add(rect_around_b1_green)
            self.wait(3)
            self.add(arrow2_green)
            self.wait(2)
            self.add(rect_around_3_green)
            element4 = nea_results_table_2.get_entries((1, 4))
            self.play(FadeIn(element4))
            self.wait(2)
            self.remove(rect_around_b1_green)

        # 3. a in sequence
        with self.voiceover(text="Das heißt, die Eingabe „a“ resultiert im Folgezustand „3“, ebenso wie die Eingabe „b“, und auch die letzte Eingabe „a“ führt zum Zustand „3“."):
            self.add(rect_around_a3_green)
            self.wait(2)
            self.add(arrow5_green)
            self.wait(1)
            self.remove(rect_around_3_green)
            self.wait(0.5)
            self.add(rect_around_3_green)
            self.wait(1)
            element5= nea_results_table_2.get_entries((1, 5))
            self.play(FadeIn(element5))
            self.wait(1)
            self.remove(rect_around_a3_green)

        # 2. b in sequence
            self.add(rect_around_b2_green)
            self.wait(1)
            self.add(arrow5_green)
            self.wait(1)
            self.remove(rect_around_3_green)
            self.wait(0.5)
            self.add(rect_around_3_green)
            self.wait(1)
            element6= nea_results_table_2.get_entries((1, 6))
            self.play(FadeIn(element6))
            self.wait(2)
            self.remove(rect_around_b2_green)
        
            # 4. a in sequenc
            self.add(rect_around_a4_green)
            self.wait(1)
            self.add(arrow5_green)
            self.wait(1)
            self.remove(rect_around_3_green)
            self.wait(0.5)
            self.add(rect_around_3_green)
            self.wait(1)
            element7= nea_results_table_2.get_entries((1, 7))
            self.play(FadeIn(element7))
            self.wait(1)
            self.remove(rect_around_a4_green)
        
        nea_results_table_2.set_color(GREEN)
        self.play(Create(nea_results_table_2))
        self.wait(1)


        with self.voiceover(text="Auch hier, sind wir fertig und wir tragen einen Check ein!"):
        # add chekmark at the end of the sequence
            checkmark2 = Text("✓", font_size=50, color=GREEN).next_to(text_sequence, RIGHT)
            self.add(checkmark2)
            self.remove(checkmark2)
            self.wait(4)

        example_group = Group(text_sequence, nea_results_table_2, self.nea_all_elements, 
                        rect_around_1_green, rect_around_2_green, rect_around_3_green,
                        arrow1_green, arrow2_green, arrow3_green, arrow4_green, arrow5_green)
        
        with self.voiceover(text="Vergleicht man die resultierenden Zustände beider Durchläufe, sieht man, dass man beim NEA im Vergleich zum DEA verschiedene Wege zum Endzustand und somit auch verschiedene resultierende Zustände hat. Das bedeutet, dass eine Sequenz akzeptiert wird, wenn es einen Weg zum Endzustand gibt. In unserem Beispiel gibt es nicht nur einen, sondern mehrere solche Wege."):
            self.play(example_group.animate.move_to(UP))
            self.wait(1)

            nea_results_table.next_to(nea_results_table_2, DOWN, buff = 0.7)
            nea_results_table.set_color(RED)
            self.play(FadeIn(nea_results_table))
            self.wait(1)
        
#########################################################
#########################DEA&NEA#########################
#########################################################

    #def dea_vs_nea(self):

        # versus
        ##self.play(FadeIn(versus_text))


        # DEA graph
        #self.play(FadeIn(dea_graph))
        #self.wait(2)  

        # a line as divider 
        #self.play(Create(divider_line))


        
        # move nea - right
        #self.play(self.nea_all_elements.animate.scale(0.6).to_edge(RIGHT, buff=0.5))
        # move title to graph
        #self.play(self.nea.animate.scale(0.7).to_edge(RIGHT, buff=2.8))
        #self.add(Text("DEA", font_size= 50).scale(0.7).to_edge(UP).to_edge(LEFT, buff=2.8))
