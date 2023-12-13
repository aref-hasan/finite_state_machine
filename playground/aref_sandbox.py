from manim import *

class CircleAnimation(Scene):
    def construct(self):
        # Erstelle einen Kreis
        circle = Circle(radius=1, color=BLUE)

        # Zeige den Kreis auf der Szene
        self.play(Create(circle))  # 'Create' fügt eine Eintrittsanimation hinzu

        # Führe eine Animation am Kreis durch (z.B. Skalierung)
        self.play(Transform(circle, circle.scale(2)))

        # Warte eine Sekunde, bevor die Animation endet
        self.wait(1)