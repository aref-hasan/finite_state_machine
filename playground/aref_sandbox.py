from manim import *

class DEA(MovingCameraScene):
    def construct(self):
        #self.DEA_elements()
        self.dea_graph()
    
    def DEA_elements(self):
        # Title created & placed at the top edge.
        title = Text("BESTANDTEILE", font_size=50)
        title.to_edge(UP)
        
        # elements list that describes the components of a DEA.
        components = VGroup(
            Text("1.  Zustände Q (endlich viele!)"),
            Text("2.  Eingabealphabet Σ"),
            Text("3.  Übergangsfunktion δ: Q x Σ -> Q"),
            Text("4.  Anfangszustand q₀ ∈ Q"),
            Text("5.  Endzustände F ⊆ Q"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)

        components.scale(0.7)  # Scale down components for fit
        components.next_to(title, DOWN, buff=0.6)
        components.to_edge(LEFT, buff=0.75)  # Move components to left edge.

        all_elements = VGroup(title, components)  # Group title & components together.
        
        # Animation section
        self.play(Write(title))  
        self.wait(4)
        self.play(title.animate.to_edge(LEFT))  # Move the title to left edge.
        self.play(LaggedStart(*[Write(comp) for comp in components], lag_ratio=0.9))  # Sequentially write the components with delay.
        self.wait(4)
        self.play(all_elements.animate.scale(0.3).to_edge(UP + LEFT, buff=0.3))  # Scale down and move all elements to top left.

        # a rectangle around all_elements after they are moved and scaled.
        surrounding_rectangle = SurroundingRectangle(all_elements, buff=.1, color="white")
        self.play(Create(surrounding_rectangle))  
        self.wait(2)  

    def sound(self):
        self.play(Write(Text("Hello World!")), run_time=3)
        
        self.add_sound("../src/sounds/pokemon_original.mp3")

        self.play(FadeOut(Text("Hello World!")), run_time=1)

    def dea_graph(self):

        self.dea_short = Text("DEA", font_size= 50)

        self.dea_long = Text("Deterministische endliche Automaten", font_size= 50)  
        
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


        self.dea_all_elements = Group(diagonal_arrow, circle1, text1c, arrow_1, label_1, arrow1, label1,
                                    arrow3, label3, circle2, text2c, arrow2, label2, circle3, text3c, arrow_3,
                                    label_3, circle_around_state3)

    

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
        
        self.wait(4)

        self.play(self.dea_all_elements.animate.next_to(self.dea_short, DOWN, buff=1.0))


# To run this scene with Manim, use the following command in the terminal:
# manim -pql aref_sandbox.py Main



