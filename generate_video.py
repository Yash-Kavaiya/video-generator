from manim import *

class MergeSortVisualization(Scene):
    def construct(self):
        # Initial array to sort
        arr = [38, 27, 43, 10, 3, 82, 9, 15]
        
        # Title
        title = Text("Merge Sort Algorithm", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Create initial array visualization
        initial_array = self.create_array_visual(arr, scale=0.8)
        initial_array.next_to(title, DOWN, buff=0.5)
        self.play(Create(initial_array))
        self.wait()
        
        # Explanation text
        explanation = Text("Divide and Conquer Approach", font_size=32, color=YELLOW)
        explanation.to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(explanation))
        
        # Start merge sort visualization
        self.merge_sort_visual(arr, initial_array)
        
        # Final message
        final_text = Text("Sorted!", font_size=48, color=GREEN)
        final_text.next_to(title, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
    
    def create_array_visual(self, arr, scale=1.0, position=ORIGIN):
        """Create visual representation of array with rectangles and numbers"""
        rectangles = VGroup()
        numbers = VGroup()
        
        for i, val in enumerate(arr):
            # Create rectangle
            rect = Rectangle(height=0.8 * scale, width=1.0 * scale)
            rect.set_stroke(WHITE, 2)
            rect.set_fill(BLUE, opacity=0.5)
            
            # Create number text
            num = Text(str(val), font_size=int(32 * scale))
            num.move_to(rect.get_center())
            
            # Position rectangle
            if i == 0:
                rect.move_to(position)
            else:
                rect.next_to(rectangles[-1], RIGHT, buff=0.1 * scale)
            
            num.move_to(rect.get_center())
            
            rectangles.add(rect)
            numbers.add(num)
        
        array_group = VGroup(rectangles, numbers)
        return array_group
    
    def merge_sort_visual(self, arr, array_visual):
        """Visualize merge sort with recursive division and merging"""
        n = len(arr)
        
        if n <= 1:
            return
        
        # Show division phase
        self.show_division(arr, array_visual)
        
        # Recursively sort and merge
        sorted_arr = self.merge_sort_recursive(arr.copy())
        
        # Create final sorted array
        final_visual = self.create_array_visual(sorted_arr, scale=0.8)
        final_visual.move_to(array_visual.get_center())
        
        self.play(
            Transform(array_visual, final_visual),
            array_visual[0].animate.set_fill(GREEN, opacity=0.7)
        )
        self.wait()
    
    def show_division(self, arr, array_visual):
        """Show the division phase of merge sort"""
        n = len(arr)
        
        if n <= 1:
            return
        
        mid = n // 2
        
        # Highlight left and right halves
        left_rects = array_visual[0][:mid]
        right_rects = array_visual[0][mid:]
        
        # Color left half
        self.play(
            left_rects.animate.set_fill(YELLOW, opacity=0.6),
            run_time=0.5
        )
        
        # Color right half
        self.play(
            right_rects.animate.set_fill(ORANGE, opacity=0.6),
            run_time=0.5
        )
        self.wait(0.5)
        
        # Show division
