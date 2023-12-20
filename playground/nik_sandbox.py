from manim import *

class FiniteStateMachine(Scene):
    def construct(self):
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

        # Keep the scene displayed
        self.wait(2)

        
# manim -pql /Users/nikyakovlev/finite_state_machine/playground/nik_sandbox.py