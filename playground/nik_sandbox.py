from manim import *

class FiniteStateMachine(Scene):
    def construct(self):
        # Load states as images
        state2_img = ImageMobject("../img/pokemon/PNG/charmeleon.png").scale(1)
        state1_img = ImageMobject("../img/pokemon/PNG/charmander.png").scale(1).next_to(state2_img, LEFT, buff=2)
        state3_img = ImageMobject("../img/pokemon/PNG/charizard.png").scale(1).next_to(state2_img, RIGHT, buff=2)


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
            MathTex(r"A \text{ finite-state transducer is a sextuple } (\Sigma, \Gamma, S, s_0, \delta, \omega), \text{ where:}").scale(0.5).next_to(state1_img, DOWN, buff=1),
            MathTex(r"\Sigma \text{ is the input alphabet (a finite non-empty set of symbols);}").scale(0.5).next_to(state1_img, DOWN, buff=1.5),
            MathTex(r"\Gamma \text{ is the output alphabet (a finite non-empty set of symbols);}").scale(0.5).next_to(state1_img, DOWN, buff=2),
            MathTex(r"S \text{ is a finite non-empty set of states;}").scale(0.5).next_to(state1_img, DOWN, buff=2.5),
            MathTex(r"s_0 \text{ is the initial state, an element of } S;").scale(0.5).next_to(state1_img, DOWN, buff=3),
            MathTex(r"\delta \text{ is the state-transition function: } S \times \Sigma \rightarrow S;").scale(0.5).next_to(state1_img, DOWN, buff=3.5),
            MathTex(r"\omega \text{ is the output function.}").scale(0.5).next_to(state1_img, DOWN, buff=4)
        ]

        # Display FSM Components
        for text_obj in fsm_components_text:
            self.play(Write(text_obj))
            self.wait(2)

        # Keep the scene displayed
        self.wait(2)
gi
        

# manim -pql /Users/nikyakovlev/finite_state_machine/playground/nik_sandbox.py