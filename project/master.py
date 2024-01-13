
from manim import *
import cv2
from manim_voiceover import VoiceoverScene
from manim.scene.moving_camera_scene import MovingCameraScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

###########################################################################################################
################################################MAIN#######################################################
###########################################################################################################

class Main(MovingCameraScene):
    def construct(self):
        #self.greeting()
        #self.welcome()
        #self.pokemon_logo()
        #self.vid()
        #self.pokemon_fig()
        #self.pokemon_components()
        #self.pokemon_components_math()
        self.dea_graph()
        self.dea_table()
        self.dea_components()
        self.dea_titles()
        self.nea_intro()
        self.nea_graph()
        self.nea_table()
        self.nea_components()
        self.nea_titles()
        #self.dea_vs_nea()

    def greeting(self):
        text = Text("Hallo Zusammen!", font_size= 50)
        self.play(Write(text))
        self.wait(3)  
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
        self.wait(4)
        
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
        circle2 = Circle(radius=0.6, color=BLUE)
        circle2.move_to(ORIGIN)
        circle1 = Circle(radius=0.6, color=BLUE).next_to(circle2, LEFT, buff=2)
        circle3 = Circle(radius=0.6, color=BLUE).next_to(circle2, RIGHT, buff=2)
        
        # text inside the circles
        self.text1c = Text("1", font_size=24).move_to(circle1.get_center())
        self.text2c = Text("2", font_size=24).move_to(circle2.get_center())
        self.text3c = Text("3", font_size=24).move_to(circle3.get_center())

        # straight arrows
        arrow1 = Arrow(start=circle1.get_top() + DOWN * 0.4, end=circle2.get_top() + DOWN * 0.4, buff=0.7) 
        arrow2 = Arrow(start=circle2.get_top() + DOWN * 0.4, end=circle3.get_top() + DOWN * 0.4, buff=0.7)
        arrow3 = Arrow(start=circle2.get_bottom() + UP * 0.4, end=circle1.get_bottom() + UP * 0.4, buff=0.7)

        # straight arrow labels
        label1 = Text("a").next_to(arrow1, UP, buff=0.1).scale(0.5)
        label2 = Text("b").next_to(arrow2, UP, buff=0.1).scale(0.5)
        label3 = Text("a").next_to(arrow3, DOWN, buff=0.1).scale(0.5)

        # double circle for circle 3
        circle_around_state3 = Circle(color=BLUE).scale(0.5)
        circle_around_state3.move_to(circle3.get_center())

        # arrow for iniial state
        start_point = circle1.get_center() + LEFT * 2 + UP * 1 
        diagonal_arrow = Arrow(start=start_point, end=circle1.get_left(), buff=0.1)

        # coordinates for curved arrows
        radius = circle1.width / 1.5
        angle = 52 * DEGREES  
        start_x = radius * np.cos(angle)/ 1.6
        start_y = radius * np.sin(angle) 
        start_point_1 = circle1.get_center() + np.array([start_x, start_y, 5])
        start_point_3 = circle3.get_center() + np.array([start_x, start_y, 5])
        end_angle = angle + 45.5
        end_x = radius * np.cos(end_angle) / 1.6 
        end_y = radius * np.sin(end_angle)
        end_point_1 = circle1.get_center() + np.array([end_x, end_y, 2])
        end_point_3 = circle3.get_center() + np.array([end_x, end_y, 2])

        # curved arrows
        arrow_1 = CurvedArrow(start_point_1, end_point_1, color=WHITE, angle= 3)
        arrow_3 = CurvedArrow(start_point_3, end_point_3, color=WHITE, angle= 3)

        # curved arrow labels
        label_1 = Text("b", font_size=24, color=WHITE)
        label_3 = Text("a, b", font_size=24, color=WHITE)
        label_offset = np.array([0.2, 0.2, 0])
        label_1.move_to(arrow_1.point_from_proportion(0.5) + label_offset)
        label_3.move_to(arrow_3.point_from_proportion(0.5) + label_offset)


        self.dea_all_elements = Group(diagonal_arrow, circle1, self.text1c, arrow_1, label_1, arrow1, label1,
                                    arrow3, label3, circle2, self.text2c, arrow2, label2, circle3, self.text3c, arrow_3,
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
        self.play(FadeIn(circle1), Write(self.text1c))
        self.wait(3)
        self.play(Create(arrow_1), Write(label_1)) 
        self.wait(3)
        self.play(Create(arrow1), Write(label1))
        self.wait(3)
        self.play(Create(arrow3), Write(label3))
        self.wait(3)
        self.play(FadeIn(circle2), Write(self.text2c))  
        self.wait(3)
        self.play(Create(arrow2), Write(label2))
        self.wait(3)
        self.play(FadeIn(circle3), Write(self.text3c))
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

        self.clear()

###########################NEA###########################
    def nea_intro(self):
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
        self.play(Write(self.dea_long), run_time=3)
        self.wait(2)  
        self.play(FadeOut(self.dea_long), run_time = 1)

        # NEA title
        self.play(Write(nea_long), run_time=3)
        self.wait(1)  
        self.play(FadeOut(nea_long))

        # NEA title shortcut
        self.play(Write(self.nea))  
        self.wait(2)

        # question mark
        self.play(Write(question_mark))
        for _ in range(2): 
            self.play(question_mark.animate.scale(1.2), run_time=0.5)
            self.play(question_mark.animate.scale(0.8), run_time=0.5)
            self.play(question_mark.animate.scale(1.2), run_time=0.5)
            self.play(question_mark.animate.scale(0.001), run_time=0.9)

        # NEA description 
        self.play(Write(nea_description))
        self.wait(6)
        self.play(FadeOut(nea_description))
        self.wait(2)

        # move NEA shortcut up
        self.play(self.nea.animate.to_edge(UP))  
        self.wait(2)
        
    def nea_graph(self):
        # The 3 begining circles
        circle2 = Circle(radius=0.6, color=BLUE)
        circle2.move_to(ORIGIN)
        circle1 = Circle(radius=0.6, color=BLUE).next_to(circle2, LEFT, buff=2)
        circle3 = Circle(radius=0.6, color=BLUE).next_to(circle2, RIGHT, buff=2)
        
        # text inside the circles
        self.text1 = Text("1", font_size=24).move_to(circle1.get_center())
        text2 = Text("2", font_size=24).move_to(circle2.get_center())
        text3 = Text("3", font_size=24).move_to(circle3.get_center())

        # straight arrows
        arrow1 = Arrow(start=circle1.get_top() + DOWN * 0.4, end=circle2.get_top() + DOWN * 0.4, buff=0.7) 
        arrow2 = Arrow(start=circle2.get_top() + DOWN * 0.4, end=circle3.get_top() + DOWN * 0.4, buff=0.7)
        arrow3 = Arrow(start=circle2.get_bottom() + UP * 0.4, end=circle1.get_bottom() + UP * 0.4, buff=0.7)

        # straight arrow labels
        label1 = Text("a").next_to(arrow1, UP, buff=0.1).scale(0.5)
        label2 = Text("b").next_to(arrow2, UP, buff=0.1).scale(0.5)
        label3 = Text("a").next_to(arrow3, DOWN, buff=0.1).scale(0.5)

        # double circle for circle 3
        circle_around_state3 = Circle(color=BLUE).scale(0.5)
        circle_around_state3.move_to(circle3.get_center())

        # arrow for iniial state
        start_point = circle1.get_center() + LEFT * 2 + UP * 1 
        diagonal_arrow = Arrow(start=start_point, end=circle1.get_left(), buff=0.1)

        # coordinates for curved arrows
        radius = circle1.width / 1.5
        angle = 52 * DEGREES  
        start_x = radius * np.cos(angle)/ 1.6
        start_y = radius * np.sin(angle) 
        start_point_1 = circle1.get_center() + np.array([start_x, start_y, 5])
        start_point_3 = circle3.get_center() + np.array([start_x, start_y, 5])
        end_angle = angle + 45.5
        end_x = radius * np.cos(end_angle) / 1.6 
        end_y = radius * np.sin(end_angle)
        end_point_1 = circle1.get_center() + np.array([end_x, end_y, 2])
        end_point_3 = circle3.get_center() + np.array([end_x, end_y, 2])

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
        red_surrounding_rectangle = SurroundingRectangle(self.label_1, buff=.1, color="red")
        red_surrounding_rectangle_a = SurroundingRectangle(label1, buff=.1, color="red")

        all_elements = Group(diagonal_arrow, circle1, self.text1, arrow_1, self.label_1, arrow1,
                            label1, arrow3, label3, circle2, text2, arrow2, label2,
                            circle3, text3, arrow_3, label_3, circle_around_state3,
                            red_surrounding_rectangle, red_surrounding_rectangle_a)
        

        # NEA right side
        nea_graph_animation = all_elements.animate.scale(0.6).to_edge(RIGHT, buff=0.5)
        nea_title_animation = self.nea.animate.scale(0.7).to_edge(RIGHT, buff=2.8)

        # DEA
        dea_title_shortcut = Text("DEA", font_size=50).scale(0.7).to_edge(UP).to_edge(LEFT, buff=2.8)
        dea_graph = self.dea_all_elements.scale(1.1).to_edge(LEFT, buff=0.5)

        #versus
        versus_text = Text("VS.",font_size=50).scale(0.7).to_edge(UP)

        #divider line
        divider_line = Line(UP*2, DOWN*2)

        ###################Scene Animations###################
        # the create of NEA graph
        self.play(Create(diagonal_arrow))
        self.wait(3)
        self.play(FadeIn(circle1), Write(self.text1))
        self.wait(3)
        self.play(Create(arrow_1), Write(self.label_1)) 
        self.wait(3)
        self.play(Create(arrow1), Write(label1))
        self.wait(3)
        self.play(Create(arrow3), Write(label3))
        self.wait(3)
        self.play(FadeIn(circle2), Write(text2))  
        self.wait(3)
        self.play(Create(arrow2), Write(label2))
        self.wait(3)
        self.play(FadeIn(circle3), Write(text3))
        self.wait(3)
        self.play(Create(arrow_3), Write(label_3))  
        self.wait(3)
        self.play(Create(circle_around_state3))
        self.wait(5)
        
        #red rectangle (a,b)
        self.play(Create(red_surrounding_rectangle))  
        self.wait(2)

        #red rectangle (a)
        self.play(Create(red_surrounding_rectangle_a))  
        self.wait(2)

        # move NEA
        nea_animations = AnimationGroup(nea_graph_animation,nea_title_animation)
        self.play(nea_animations)
        
        # show DEA 
        # DEA title
        self.play(FadeIn(dea_title_shortcut, shift=DOWN))
        self.wait(2)

        # DEA graph 
        self.play(FadeIn(dea_graph))
        self.wait(3)  

        # Fadeout DEA 
        self.play(FadeOut(dea_graph,dea_title_shortcut))
        self.wait(1)

        # move NEA title back
        nea_title_animation = self.nea.animate.move_to(UP * 3.5)  
        self.play(nea_title_animation)

        # move NEA graph back
        nea_graph_animation = all_elements.animate.next_to(self.nea, UP, buff= - 2.4)
        red_surrounding_rectangle_animation = FadeOut(red_surrounding_rectangle)
        red_surrounding_rectangle_a_animation = FadeOut(red_surrounding_rectangle_a)

        #Group all animation
        nea_animations = AnimationGroup(red_surrounding_rectangle_animation, red_surrounding_rectangle_a_animation, 
                                        nea_graph_animation)

        self.play(nea_animations)
        self.wait(4)

    def nea_table(self):

        custom_values = [
            [" ", "a", "b"],
            [1, 2, 1],
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
        text1 = Text("Zustand", font_size=36, color=WHITE)
        text1.next_to(self.nea_t1.get_cell((2, 1)), LEFT, buff=1)
        arrow1 = Arrow(text1.get_right(), self.nea_t1.get_cell((2, 1)).get_left(), buff=0.1)

        # Adding text with an arrow
        text2 = Text("Übergang", font_size=36, color=WHITE)
        text2.next_to(self.nea_t1.get_cell((1, 3)), RIGHT, buff=1)
        arrow2 = Arrow(text2.get_left(), self.nea_t1.get_cell((1, 3)).get_right(), buff=0.1)

        # Adding text with an arrow
        text3 = Text("resultierender Zustand", font_size=36, color=WHITE)
        text3.next_to(self.nea_t1.get_cell((2, 3)), RIGHT, buff=1)
        arrow3 = Arrow(text3.get_left(), self.nea_t1.get_cell((2, 3)).get_right(), buff=0.1)


        red_rectangle1 = Rectangle(color=RED).scale(0.3)
        red_rectangle1.surround(self.text1)

        red_rectangle2 = Rectangle(color=RED).scale(0.3)
        red_rectangle2.surround(self.label_1)


        # table
        self.play(Create(self.nea_t1))
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

        self.play(self.nea_t1.animate.to_edge(LEFT))
        self.wait(2)

    def nea_components(self):
        self.components_text= VGroup(
            MathTex("Q = \\{1, 2, 3\\}"),
            MathTex("\Sigma = \\{a, b\\}"),
            MathTex(r"\delta : 1 + a \rightarrow 2 ; 1 + b \rightarrow 1 ; 2 + a \rightarrow 1 ;"),
            MathTex(r"  2 + b \rightarrow 3 ; 3 + a \rightarrow 3 ; 3 + b \rightarrow 3"),
            MathTex(r"q_0 = 1 \in Q"),
            MathTex(r"F = \{3\} \subseteq Q")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.components_text.scale(0.7)
        self.components_text.next_to(self.t1.get_cell((2, 3)), RIGHT, buff=3.5)
        self.play(LaggedStart(*[Write(comp) for comp in self.components_text], lag_ratio=0.9))  # Sequentially write the components with delay.
        self.wait(2)  
        self.play(self.components_text.animate.scale(0.85).to_edge(RIGHT + DOWN, buff=1))
        
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

        self.clear()
    #def dea_vs_nea(self):

        # versus
        ##self.play(FadeIn(versus_text))


        # DEA graph
        #self.play(FadeIn(dea_graph))
        #self.wait(2)  

        # a line as divider 
        #self.play(Create(divider_line))


        
        # move nea - right
        #self.play(all_elements.animate.scale(0.6).to_edge(RIGHT, buff=0.5))
        # move title to graph
        #self.play(self.nea.animate.scale(0.7).to_edge(RIGHT, buff=2.8))
        #self.add(Text("DEA", font_size= 50).scale(0.7).to_edge(UP).to_edge(LEFT, buff=2.8))
