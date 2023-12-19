from manim import *


class Main(MovingCameraScene):
    def construct(self):
        self.test()

    def test(self):
        # Titel hinzufügen
        

        # Liste der Bestandteile eines endlichen Automaten
        # Jede Zeile ist ein eigenes Text-Objekt
        components = VGroup(
            Text("1. Zustände Q (endlich viele!)"),
            Text("2. Eingabealphabet Σ"),
            Text("3. Übergangsfunktion δ: Q x Σ -> Q"),
            Text("4. Anfangszustand q₀ ∈ Q"),
            Text("5. Endzustände F ⊆ Q"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=1)

        components.scale(0.7)  # Größenanpassung, falls nötig

        # Animation
        #self.play(Write(title))
        self.play(Write(components))
        self.wait(2)

# Zum Rendern der Szene verwenden Sie den folgenden Befehl in der Kommandozeile:
# manim -pql script_name.py FiniteAutomataComponents
