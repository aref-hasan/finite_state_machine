from manim import *

class TableScene(Scene):
    def construct(self):
        # Erstellen der Tabelle mit den Daten        
        text_sequence = Text("Sequenz: a a b a b a", font_size=35).next_to(self.nea_circle2, DOWN, buff=1)

        results_data = [["-> 1", "2", "1", "1", "2", "3", "3"]]
        nea_results_table = Table(results_data, include_outer_lines=True).scale(0.4)
        # Positionieren der Tabelle
        nea_results_table.next_to(text_sequence, DOWN, buff=0.35)

        # Erstellen einer leeren Tabelle mit gleicher Größe und Position
        empty_table = Table([["" for _ in range(len(results_data[0]))]], include_outer_lines=True).scale(0.4)
        empty_table.move_to(nea_results_table)

        # Fügen Sie die leere Tabelle der Szene hinzu
        self.add(empty_table)

        # Schrittweise das Hinzufügen der Elemente
        for row in range(len(results_data)):
            for col in range(len(results_data[row])):
                # Erstellen des Elements, das hinzugefügt werden soll
                element = nea_results_table.get_entries((row+1, col+1))
                # Hinzufügen des Elements zur Szene
                self.play(FadeIn(element))

        # Alternative: Verwenden von Write statt FadeIn
        # self.play(Write(nea_results_table))
