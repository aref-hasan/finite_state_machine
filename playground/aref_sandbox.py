from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim import *

class MyAwesomeScene(VoiceoverScene):
    def construct(self):
        circle = Circle(radius=0.6, color=BLUE)
        self.set_speech_service(GTTSService(lang="de"))  # Setzt die Sprache auf Deutsch
        with self.voiceover(text="Dieser Kreis wird gezeichnet, während ich spreche.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
