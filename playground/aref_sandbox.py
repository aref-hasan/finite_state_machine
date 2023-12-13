from manim import *

class CircleWithArrow(Scene):
    def construct(self):
        # Erstelle einen Kreis
        outer_circle = Circle(color=RED)
        inner_circle = Circle(color=WHITE)

        # Definiere den Startpunkt des Pfeils außerhalb des äußeren Kreises
        arrow_start_angle = 0  # Kann auf jeden Winkel zwischen 0 und 2*PI gesetzt werden
        arrow_start_point = outer_circle.point_at_angle(arrow_start_angle) + (outer_circle.radius + 0.5) * RIGHT

        # Der Endpunkt des Pfeils ist ein Punkt auf dem Umfang des inneren Kreises
        arrow_end_point = inner_circle.point_at_angle(arrow_start_angle)

        # Erstelle den Pfeil
        arrow = Arrow(arrow_start_point, arrow_end_point, buff=0, color=WHITE)

        # Zeige den inneren und äußeren Kreis und den Pfeil an
        self.play(Create(outer_circle), Create(inner_circle))
        self.play(Create(arrow))
        self.wait(1)
