from manim import *

class FiniteStateMachine(Scene):
    def construct(self):
        # Erstellen eines Textobjekts mit zwei Zeilen
        welcome_text = Text("Herzlich willkommen zu unserem\nVideo über Zustandsautomaten!", 
                            font_size=48, 
                            color=WHITE)

        # Zentrieren des Textes
        welcome_text.move_to(ORIGIN)

        # Erstellen einer Animation, um den Text anzuzeigen
        self.play(Write(welcome_text))

        # Den Text für eine Weile auf dem Bildschirm halten
        self.wait(2)

        # Den Text ausblenden
        self.play(FadeOut(welcome_text))

        # Laden des Bildes (ersetzen Sie 'pfad/zum/bild.png' mit dem tatsächlichen Pfad zu Ihrem Bild)
        image = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/pokemon_logo.png").scale(0.7)

        # Zentrieren des Bildes
        image.move_to(ORIGIN)

        # Einblenden des Bildes
        self.play(FadeIn(image))

        # Warten
        self.wait(2)

        # Ausblenden des Bildes, indem es schrumpft
        self.play(ShrinkToCenter(image))


        # Load states as images
        state2_img = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charmeleon.png").scale(1)
        state1_img = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charmander.png").scale(1).next_to(state2_img, LEFT, buff=2)
        state3_img = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charizard.png").scale(1).next_to(state2_img, RIGHT, buff=2)
        

        # Define transitions
        arrow1 = Arrow(start=state1_img.get_right(), end=state2_img.get_left(), buff=0.3)
        arrow2 = Arrow(start=state2_img.get_right(), end=state3_img.get_left(), buff=0.3)
        label1 = Text("Lvl 16").next_to(arrow1, UP, buff=0.1).scale(0.5)
        label2 = Text("Lvl 36").next_to(arrow2, UP, buff=0.1).scale(0.5)

        # Create a white circle around state3_img
        circle_around_state3 = Circle(color=WHITE).scale(1.2)
        circle_around_state3.move_to(state3_img.get_center())

        # Create a diagonal arrow pointing to state1_img
        start_point = state1_img.get_center() + LEFT * 2 + UP * 1  # Adjust as needed
        diagonal_arrow = Arrow(start=start_point, end=state1_img.get_left(), buff=0.1)

        all_elements = Group(state1_img, state2_img, state3_img, arrow1, arrow2, label1, label2, circle_around_state3, diagonal_arrow)


        # Add states and transitions to the scene
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

        # FSM Components as Text
        fsm_components_text = [
            MathTex(r"Ein \text{ endlicher Automat ist ein 5-Tupel } (Q, \Sigma, \delta, q_0, F), \text{ wobei:}").scale(0.5).next_to(state1_img, DOWN, buff=0.5),
            MathTex(r"Q \text{ ist eine endliche Menge von Zuständen;}").scale(0.5).next_to(state1_img, DOWN, buff=1.5),
            MathTex(r"\Sigma \text{ ist das Eingabealphabet (eine endliche nicht-leere Menge von Symbolen);}").scale(0.5).next_to(state1_img, DOWN, buff=2.5),
            MathTex(r"\delta \text{ ist die Zustandsübergangsfunktion: } Q \times \Sigma \rightarrow Q;").scale(0.5).next_to(state1_img, DOWN, buff=3.5),
            MathTex(r"q_0 \text{ ist der Anfangszustand, ein Element von } Q;").scale(0.5).next_to(state1_img, DOWN, buff=4.5),
            MathTex(r"F \text{ ist die Menge der Endzustände, eine Teilmenge von } Q.").scale(0.5).next_to(state1_img, DOWN, buff=5.5)
        ]


        # Display FSM Components
        for text_obj in fsm_components_text:
            self.play(Write(text_obj))
            self.wait(2)

        # Text parts of the expression
        text1 = MathTex("Q = \\{").scale(0.5)
        text2 = MathTex("\\}").scale(0.5)
        text3 = MathTex(",").scale(0.5)
        text4 = MathTex(",").scale(0.5)

        # Image objects (replace 'image_path' with the path to your images)
        image1 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charmander.png").scale(0.2)
        image2 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charmeleon.png").scale(0.2)
        image3 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charizard.png").scale(0.2)

        # Positioning the objects
        text1.next_to(fsm_components_text[1], RIGHT, buff=3)
        image1.next_to(text1, RIGHT, buff=0.1)
        text3.next_to(image1, RIGHT, buff=0.1)
        image2.next_to(text3, RIGHT, buff=0.1)
        text4.next_to(image2, RIGHT, buff=0.1)
        image3.next_to(text4, RIGHT, buff=0.1)
        text2.next_to(image3, RIGHT, buff=0.1)

        # Add objects to the scene
        self.add(text1, image1, text3, image2, text4, image3, text2)

        # Text parts of the expression
        text1 = MathTex("\Sigma = \\{").scale(0.5)
        text2 = MathTex("\\}").scale(0.5)
        text3 = MathTex(",").scale(0.5)
        

        # Image objects (replace 'image_path' with the path to your images)
        text16 = Text("Lvl 16").scale(0.3)
        text36 = Text("Lvl 36").scale(0.3)

        # Positioning the objects
        text1.next_to(fsm_components_text[2], RIGHT, buff=1.2)
        text16.next_to(text1, RIGHT, buff=0.1)
        text3.next_to(text16, RIGHT, buff=0.1)
        text36.next_to(text3, RIGHT, buff=0.1)
        text2.next_to(text36, RIGHT, buff=0.1)

        # Add objects to the scene
        self.add(text1, text16, text3, text36, text2)

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
        image1 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charmander.png").scale(0.2)
        image2 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charmeleon.png").scale(0.2)
        image2_2 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charmeleon.png").scale(0.2)
        image3 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charizard.png").scale(0.2)

        # Positioning the objects
        text1.next_to(fsm_components_text[3], RIGHT, buff=1.2)
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

         # Text parts of the expression
        text1 = MathTex(r"q_0 = ").scale(0.5)
        text2 = MathTex(r"\in Q").scale(0.5)

        # Image objects (replace 'image_path' with the path to your images)
        image1 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charmander.png").scale(0.2)

        # Positioning the objects
        text1.next_to(fsm_components_text[4], RIGHT, buff=3.1)
        image1.next_to(text1, RIGHT, buff=0.1)
        text2.next_to(image1, RIGHT, buff=0.1)
    
        # Add objects to the scene
        self.add(text1, image1, text2)

          # Text parts of the expression
        text1 = MathTex(r"F = \{").scale(0.5)
        text2 = MathTex(r"\} \subseteq Q").scale(0.5)

        # Image objects (replace 'image_path' with the path to your images)
        image1 = ImageMobject("/Users/nikyakovlev/finite_state_machine/src/img/pokemon/PNG/charizard.png").scale(0.2)

        # Positioning the objects
        text1.next_to(fsm_components_text[5], RIGHT, buff=2.4)
        image1.next_to(text1, RIGHT, buff=0.1)
        text2.next_to(image1, RIGHT, buff=0.1)
    
        # Add objects to the scene
        self.add(text1, image1, text2)

        # Keep the scene displayed
        self.wait(2)

        self.clear()



        ################################# new image ######################################################

        # The 3 begining circles
        circle2 = Circle(radius=0.6, color=BLUE)
        circle2.move_to(ORIGIN)
        circle1 = Circle(radius=0.6, color=BLUE).next_to(circle2, LEFT, buff=2)
        circle3 = Circle(radius=0.6, color=BLUE).next_to(circle2, RIGHT, buff=2)
        
        # text inside the circles
        text1c = Text("1", font_size=24).move_to(circle1.get_center())
        text2c = Text("2", font_size=24).move_to(circle2.get_center())
        text3c = Text("3", font_size=24).move_to(circle3.get_center())

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


        all_elements = Group(diagonal_arrow, circle1, text1c, arrow_1, label_1, arrow1, label1, arrow3, label3, circle2, text2c, arrow2, label2, circle3, text3c, arrow_3, label_3, circle_around_state3)


        self.play(Create(diagonal_arrow))
        self.wait(3)
        self.play(FadeIn(circle1), Write(text1c))
        self.wait(3)
        self.play(Create(arrow_1), Write(label_1)) 
        self.wait(3)
        self.play(Create(arrow1), Write(label1))
        self.wait(3)
        self.play(Create(arrow3), Write(label3))
        self.wait(3)
        self.play(FadeIn(circle2), Write(text2c))  
        self.wait(3)
        self.play(Create(arrow2), Write(label2))
        self.wait(3)
        self.play(FadeIn(circle3), Write(text3c))
        self.wait(3)
        self.play(Create(arrow_3), Write(label_3))  
        self.wait(3)
        self.play(Create(circle_around_state3))

        self.play(all_elements.animate.scale(0.6).to_edge(UP))


        custom_values = [
            [" ", "a", "b"],
            [1, 2, 1],
            [2, 1, 3],
            [3, 3, 3]
        ]
        string_values = [[str(item) for item in row] for row in custom_values]

        # Create a table with the custom values
        t1 = Table(
            string_values,
            include_outer_lines=True
        ).scale(0.7)

        # Color the first row and first column red
        
        t1.add_highlighted_cell((1, 2), color=RED)
        t1.add_highlighted_cell((1, 3), color=RED)
        t1.add_highlighted_cell((2, 1), color=RED)
        t1.add_highlighted_cell((3, 1), color=RED)
        t1.add_highlighted_cell((4, 1), color=RED)


        # Move the table to the left lower corner
        t1.to_corner(DOWN)

        # Adding text with an arrow
        text1 = Text("Zustand", font_size=36, color=WHITE)
        text1.next_to(t1.get_cell((2, 1)), LEFT, buff=1)
        arrow1 = Arrow(text1.get_right(), t1.get_cell((2, 1)).get_left(), buff=0.1)

        # Adding text with an arrow
        text2 = Text("Übergang", font_size=36, color=WHITE)
        text2.next_to(t1.get_cell((1, 3)), UP, buff=1)
        arrow2 = Arrow(text2.get_bottom(), t1.get_cell((1, 3)).get_top(), buff=0.1)

        # Adding text with an arrow
        text3 = Text("resultierender Zustand", font_size=36, color=WHITE)
        text3.next_to(t1.get_cell((2, 3)), RIGHT, buff=1)
        arrow3 = Arrow(text3.get_left(), t1.get_cell((2, 3)).get_right(), buff=0.1)

        red_rectangle1 = Rectangle(color=RED).scale(0.3)
        red_rectangle1.surround(text1c)

        red_rectangle2 = Rectangle(color=RED).scale(0.3)
        red_rectangle2.surround(label_1)

        red_rectangle1 = Rectangle(color=RED).scale(0.3)
        red_rectangle1.surround(text1c)

        # Play the animation to create the table
        self.play(Create(t1))
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


        self.remove(text1, arrow1, text2, arrow2, text3, arrow3, red_rectangle1)
        self.wait(2)

        self.play(t1.animate.to_edge(LEFT))
        self.wait(2)

        ##################### Bestandteile #############################
        self.components = VGroup(
            MathTex("Q = \\{1, 2, 3\\}"),
            MathTex("\Sigma = \\{a, b\\}"),
            MathTex(r"\delta : 1 + a \rightarrow 2 ; 1 + b \rightarrow 1 ; 2 + a \rightarrow 1 ;"),
            MathTex(r"  2 + b \rightarrow 3 ; 3 + a \rightarrow 3 ; 3 + b \rightarrow 3"),
            MathTex(r"q_0 = 1 \in Q"),
            MathTex(r"F = \{3\} \subseteq Q")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        self.components.scale(0.7)
        self.components.next_to(t1.get_cell((2, 3)), RIGHT, buff=3.5)
        self.play(LaggedStart(*[Write(comp) for comp in self.components], lag_ratio=0.9))  # Sequentially write the components with delay.
        self.wait(2)  
        self.play(self.components.animate.scale(0.8).to_edge(RIGHT + DOWN, buff=1))
        self.surrounding_rectangle = SurroundingRectangle(self.components, buff=.1, color="white")
        self.play(Create(self.surrounding_rectangle)) 
        self.wait(4)

        # remove table and bestandteile
        self.remove(self.components, t1, self.surrounding_rectangle)
        self.wait(4)

        # enlargen Übergangsdiagramm
        self.play(all_elements.animate.move_to(ORIGIN + LEFT * 0.6))
        self.play(all_elements.animate.scale(1/0.6))

        # add test sequence
        text_sequence = Text("Sequenz: a a b a b a", font_size=35).next_to(circle2, DOWN, buff=1)

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
        rect_around_1 = SurroundingRectangle(text1c, color=RED)       
        rect_around_2 = SurroundingRectangle(text2c, color=RED)
        rect_around_3 = SurroundingRectangle(text3c, color=RED)


        arrow1_red = Arrow(start=circle1.get_top() + DOWN * 0.4, end=circle2.get_top() + DOWN * 0.4, buff=0.7, color=RED) 
        arrow2_red = Arrow(start=circle2.get_top() + DOWN * 0.4, end=circle3.get_top() + DOWN * 0.4, buff=0.7, color=RED)
        arrow3_red = Arrow(start=circle2.get_bottom() + UP * 0.4, end=circle1.get_bottom() + UP * 0.4, buff=0.7, color=RED)

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



        
# manim -pql /Users/nikyakovlev/finite_state_machine/playground/nik_sandbox.py