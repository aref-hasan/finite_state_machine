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
        label1 = Text("Lvl 16").next_to(arrow1, UP, buff=0.1)
        label2 = Text("Lvl 36").next_to(arrow2, UP, buff=0.1)

        # Create a white circle around state3_img
        circle_around_state3 = Circle(color=WHITE).scale(1.2)
        circle_around_state3.move_to(state3_img.get_center())


        # Add states and transitions to the scene
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

        # Keep the scene displayed
        self.wait(2)


# manim -pql /Users/nikyakovlev/finite_state_machine/playground/nik_sandbox.py