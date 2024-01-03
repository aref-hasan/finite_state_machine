from manim import *
from manim import Scene

class objects(Scene):
    #hier auskommentieren was abgespielt werden sollte
    def construct(self):
        #self.greeting()
        #self.table_open()
        #self.table()
        #self.rahmen()
        #self.topics_listing()
        #self.circle_state()
        #self.circle_x()
        #self.circle_final_state()
        self.circle_self()
    def greeting(self):
        text = Text("Hallo Zusammen!", font_size= 50)
        self.play(Write(text))
        self.wait(2)  
        self.clear()

    def table_open(self):
        t0 = Table(
                [["First", "Second"],
                ["Third","Fourth"]],
                row_labels=[Text("R1"), Text("R2")],
                col_labels=[Text("C1"), Text("C2")],
                top_left_entry=Text("TOP"))
        self.play(Create(t0))
        self.wait(4)
        self.clear()

        self.clear()
    def table(self):
        vals = np.arange(1,21).reshape(5,4)
        t1 = IntegerTable(
            vals,
            include_outer_lines=True
        )
        self.play(Create(t1))
        self.wait(4)

        self.clear()

    def rahmen(self):
        top_line = Line([-2.5, 1, 0], [2.5, 1, 0])
        bottom_line = Line([-2.5, -1.5, 0], [2.5, -1.5, 0])
        left_line = Line([-2.5, 1, 0], [-2.5, -1.5, 0])
        right_line = Line([2.5, 1, 0], [2.5, -1.5, 0])
        self.play(Create(top_line), Create(bottom_line), Create(left_line), Create(right_line))
        self.wait(2)
        self.clear()

    def topics_listing(self):
        text1 = Text("1. THEMA").set_color(WHITE)

        text2 = Text("2. THEMA").set_color(WHITE)

        text3 = Text("3. THEMA").set_color(WHITE)

        text4 = Text("4. THEMA").set_color(WHITE)

        x = VGroup(text1, text2, text3, text4).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.).next_to(ORIGIN,DR)
        x.set_opacity(0.5)
        x.submobjects[1].set_opacity(1)
        self.add(x)
        self.wait(2)
        self.clear()

    def circle_state(self):
        circle = Circle(radius=0.6, color=BLUE)

        self.play(Create(circle)) 

        self.wait(1)
        self.clear()

    def circle_x(self):
        circle = Circle(radius=0.6, color=BLUE)

        line1 = Line(start=circle.get_left(), end=circle.get_right(), color=BLUE)
        line2 = Line(start=circle.get_bottom(), end=circle.get_top(), color=BLUE)

        self.play(Create(circle))
        self.play(Create(line1), Create(line2))
        self.wait(2)
        self.clear()

    def circle_final_state(self):
        outer_circle = Circle(radius=0.6, color=BLUE)

        inner_circle = Circle(radius=0.42, color=BLUE)

        inner_circle.move_to(outer_circle.get_center())
        self.play(Create(outer_circle))
        self.play(Create(inner_circle))
        self.wait(2)
        self.clear()

    def circle_self(self):
        circle = Circle(color=RED)
        self.play(Create(circle))

        radius = circle.width / 1.5
        angle = 52 * DEGREES  

        start_x = radius * np.cos(angle)/ 1.6
        start_y = radius * np.sin(angle) 
        start_point = circle.get_center() + np.array([start_x, start_y, 5])

        end_angle = angle + 45.5
        end_x = radius * np.cos(end_angle) / 1.6 
        end_y = radius * np.sin(end_angle)
        end_point = circle.get_center() + np.array([end_x, end_y, 2])

        arrow = CurvedArrow(start_point, end_point, color=WHITE, angle= 3)
        self.play(Create(arrow))

        self.wait(1)