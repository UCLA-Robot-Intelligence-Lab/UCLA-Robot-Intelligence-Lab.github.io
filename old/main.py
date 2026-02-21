from manim import *

config.media_width = "100%"
config.verbosity = "WARNING"

# introduces second law of motion, newton's first law, and newton's law of gravitation
class uril(Scene):
    def construct(self):
        full_text1 = Text("UCLA", color="#3490ce", font="Helvetica Neue", weight=BOLD)
        full_text1.move_to(LEFT * 4.8)
        single_letter1 = Text("U", color="#3490ce", font="Helvetica Neue", weight=BOLD)
        single_letter1.move_to(full_text1.get_left() + 0.2 * RIGHT)
        
        full_text2 = Text("ROBOT", color="#18315b", font="Helvetica Neue", weight=BOLD)
        full_text2.move_to(LEFT * 2.36)
        single_letter2 = Text("R", color="#18315b", font="Helvetica Neue", weight=BOLD)
        single_letter2.move_to(full_text2.get_left() + 0.2 * RIGHT)
        
        full_text3 = Text("INTELLIGENCE", color="#18315b", font="Helvetica Neue", weight=BOLD)
        full_text3.move_to(RIGHT * 1.64)
        single_letter3 = Text("I", color="#18315b", font="Helvetica Neue", weight=BOLD)
        single_letter3.move_to(full_text3.get_left() + 0.05 * RIGHT)
        
        full_text4 = Text("LAB", color="#18315b", font="Helvetica Neue", weight=BOLD)
        full_text4.move_to(RIGHT * 5.1)
        single_letter4 = Text("L", color="#18315b", font="Helvetica Neue", weight=BOLD)
        single_letter4.move_to(full_text4.get_left() + 0.16 * RIGHT)
        
        self.play(Write(full_text1), Write(full_text2), Write(full_text3), Write(full_text4))
        self.wait(1)
        
        # Change from full words to URIL
        self.play(
            ReplacementTransform(full_text1, single_letter1),
            FadeTransformPieces(full_text2, single_letter2),
            FadeTransformPieces(full_text3, single_letter3),
            FadeTransformPieces(full_text4, single_letter4)
        )
        
        # image = ImageMobject("logo.png")
        # image.scale(0.6)
        # image.move_to(ORIGIN + LEFT * 2.5)
        # # move URIL to center
        # self.play(
        #     single_letter1.animate.move_to(ORIGIN + LEFT * 0.75),
        #     single_letter2.animate.move_to(ORIGIN + LEFT * 0.25),
        #     single_letter3.animate.move_to(ORIGIN + RIGHT * 0.1),
        #     single_letter4.animate.move_to(ORIGIN + RIGHT * 0.4)
        # )
        # self.play(FadeIn(image))
        
        
        image = ImageMobject("static/transparent_logo.png")
        image.scale(0.3)
        image.move_to(ORIGIN + LEFT * 3.2 + UP * 0.3)
        # move URIL to center
        self.play(
            single_letter1.animate.move_to(ORIGIN + LEFT * 1.3).scale(4),
            single_letter2.animate.move_to(ORIGIN + RIGHT * 0.59).scale(4),
            single_letter3.animate.move_to(ORIGIN + RIGHT * 1.92).scale(4),
            single_letter4.animate.move_to(ORIGIN + RIGHT * 3.1).scale(4)
        )
        self.play(FadeIn(image))
        self.wait(2)        
        
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        
        full_text1 = Text("UCLA", color="#3490ce", font="Helvetica Neue", weight=BOLD)
        full_text1.move_to(LEFT * 4.8)
        single_letter1 = Text("U", color="#3490ce", font="Helvetica Neue", weight=BOLD)
        single_letter1.move_to(full_text1.get_left() + 0.2 * RIGHT)
        
        full_text2 = Text("ROBOT", color="#18315b", font="Helvetica Neue", weight=BOLD)
        full_text2.move_to(LEFT * 2.36)
        single_letter2 = Text("R", color="#18315b", font="Helvetica Neue", weight=BOLD)
        single_letter2.move_to(full_text2.get_left() + 0.2 * RIGHT)
        
        full_text3 = Text("INTELLIGENCE", color="#18315b", font="Helvetica Neue", weight=BOLD)
        full_text3.move_to(RIGHT * 1.64)
        single_letter3 = Text("I", color="#18315b", font="Helvetica Neue", weight=BOLD)
        single_letter3.move_to(full_text3.get_left() + 0.05 * RIGHT)
        
        full_text4 = Text("LAB", color="#18315b", font="Helvetica Neue", weight=BOLD)
        full_text4.move_to(RIGHT * 5.1)
        single_letter4 = Text("L", color="#18315b", font="Helvetica Neue", weight=BOLD)
        single_letter4.move_to(full_text4.get_left() + 0.16 * RIGHT)
        
        for letter in full_text1:
            self.play(Write(letter), run_time = 0.05)
            
        for letter in full_text2:
            self.play(Write(letter), run_time = 0.05)
            
        for letter in full_text3:
            self.play(Write(letter), run_time = 0.05)
            
        for letter in full_text4:
            self.play(Write(letter), run_time = 0.05)
            
        self.wait(1)
        
        self.wait()

