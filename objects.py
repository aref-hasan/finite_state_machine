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
        #self.circel_state()
        #self.circel_x()
        self.circel_final_state()

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

    def circel_state(self):
        circle = Circle(radius=0.6, color=BLUE)

        self.play(Create(circle)) 

        self.wait(1)
        self.clear()

    def circel_x(self):
        circle = Circle(radius=0.6, color=BLUE)

        line1 = Line(start=circle.get_left(), end=circle.get_right(), color=BLUE)
        line2 = Line(start=circle.get_bottom(), end=circle.get_top(), color=BLUE)

        self.play(Create(circle))
        self.play(Create(line1), Create(line2))
        self.wait(2)
        self.clear()

    def circel_final_state(self):
        outer_circle = Circle(radius=0.6, color=BLUE)

        inner_circle = Circle(radius=0.42, color=BLUE)

        inner_circle.move_to(outer_circle.get_center())
        self.play(Create(outer_circle))
        self.play(Create(inner_circle))
        self.wait(2)
        self.clear()
