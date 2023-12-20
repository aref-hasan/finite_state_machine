from manim import *

class DEA(MovingCameraScene):
    def construct(self):
        # Uncomment the next line if you want to start with the greeting.
        # self.greeting()
        self.DEA_elements()

    def greeting(self):
        # This function displays a greeting text.
        text = Text("Hallo Zusammen!", font_size=50)
        self.play(Write(text))
        self.wait(2)
        self.clear()  # Clears the screen after showing the greeting.

    def DEA_elements(self):
        # Title of the section is created and placed at the top edge.
        title = Text("BESTANDTEILE", font_size=50)
        title.to_edge(UP)
        
        # Creation of the elements list that describes the components of a DEA.
        components = VGroup(
            Text("1.  Zustände Q (endlich viele!)"),
            Text("2.  Eingabealphabet Σ"),
            Text("3.  Übergangsfunktion δ: Q x Σ -> Q"),
            Text("4.  Anfangszustand q₀ ∈ Q"),
            Text("5.  Endzustände F ⊆ Q"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        components.scale(0.7)  # Scale down the components for fit
        components.next_to(title, DOWN, buff=0.6)
        components.to_edge(LEFT, buff=0.75)  # Move the components to the left edge.

        all_elements = VGroup(title, components)  # Group title and components together.
        
        # Animation section
        self.play(Write(title))  # Animate the writing of the title.
        self.wait(4)
        self.play(title.animate.to_edge(LEFT))  # Move the title to the left edge.
        self.play(LaggedStart(*[Write(comp) for comp in components], lag_ratio=0.9))  # Sequentially write the components with delay.
        self.wait(4)
        self.play(all_elements.animate.scale(0.3).to_edge(UP + LEFT, buff=0.3))  # Scale down and move all elements to the top left.

        # Create a rectangle around all_elements after they are moved and scaled.
        surrounding_rectangle = SurroundingRectangle(all_elements, buff=.1, color="white")
        self.play(Create(surrounding_rectangle))  # Animate the creation of the rectangle.
        self.wait(2)  # Pause for 2 seconds after the animation.

# To run this scene with Manim, use the following command in the terminal:
# manim -pql aref_sandbox.py Main
