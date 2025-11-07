from manim import *

class BubbleSortGoogleTheme(Scene):
    def construct(self):
        # === Title ===
        title = Text("Bubble Sort Algorithm", font_size=40, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(1)

        # === Google Theme Colors ===
        google_colors = [BLUE, RED, YELLOW, GREEN, RED, BLUE]

        # === Array Elements ===
        array_values = [5, 1, 4, 2, 8]
        boxes = VGroup()
        for i, val in enumerate(array_values):
            rect = Square(side_length=1, color=google_colors[i % len(google_colors)], fill_opacity=0.3)
            num = Text(str(val), font_size=28)
            group = VGroup(rect, num)
            num.move_to(rect.get_center())
            boxes.add(group)
        boxes.arrange(RIGHT, buff=0.5)
        boxes.scale(0.9)
        boxes.move_to(ORIGIN)
        self.play(Create(boxes))
        self.wait(1)

        # === Narration Text (Step 1) ===
        narration1 = Paragraph(
            "Bubble Sort works by repeatedly swapping adjacent elements",
            "if they are in the wrong order.",
            font_size=22, alignment="center", width=6
        )
        narration1.to_edge(DOWN, buff=0.5)
        self.play(Write(narration1))
        self.wait(2)

        # === Bubble Sort Animation ===
        # We'll simulate the swapping visually
        for i in range(len(array_values) - 1):
            for j in range(len(array_values) - i - 1):
                box1 = boxes[j]
                box2 = boxes[j + 1]

                # Highlight boxes being compared
                self.play(box1.animate.set_color(YELLOW), box2.animate.set_color(YELLOW))
                self.wait(0.5)

                val1 = int(box1[1].text)
                val2 = int(box2[1].text)

                # If out of order, swap
                if val1 > val2:
                    self.play(Swap(box1, box2))
                    boxes[j], boxes[j + 1] = boxes[j + 1], boxes[j]
                    self.wait(0.5)

                # Reset colors
                self.play(box1.animate.set_color(google_colors[j % len(google_colors)]),
                          box2.animate.set_color(google_colors[(j + 1) % len(google_colors)]))
                self.wait(0.3)

        # === Narration Text (Step 2) ===
        self.play(FadeOut(narration1))
        narration2 = Paragraph(
            "After each pass, the largest unsorted element",
            "bubbles up to its correct position at the end.",
            font_size=22, alignment="center", width=6
        )
        narration2.to_edge(DOWN, buff=0.5)
        self.play(Write(narration2))
        self.wait(2)

        # === Final Sorted Array ===
        sorted_label = Text("Sorted Array", font_size=28, color=GREEN)
        sorted_label.next_to(boxes, UP, buff=0.5)
        self.play(Write(sorted_label))
        self.wait(1)

        # Highlight final order
        self.play(boxes.animate.set_color(GREEN))
        self.wait(2)

        # === Fade Out Everything ===
        self.play(FadeOut(VGroup(boxes, sorted_label, narration2, title)))
        self.wait()

