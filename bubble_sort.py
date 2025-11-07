import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

class MergeSortAnimator:
    def __init__(self, arr_size=10, max_value=50):
        """
        Initialize the animator with a random array.
        :param arr_size: Size of the array to sort.
        :param max_value: Maximum value in the array.
        """
        self.original_arr = [random.randint(1, max_value) for _ in range(arr_size)]
        self.arr = self.original_arr.copy()
        self.states = []  # List of (array_copy, colors, text) for each frame
        self.width = 2  # Bar width for visualization
        self.height_scale = 10  # Scale for bar heights

    def merge(self, left, mid, right):
        """
        Merge two sorted halves and record states for animation.
        :param left: Start index of left subarray.
        :param mid: End index of left subarray.
        :param right: End index of right subarray.
        """
        n1 = mid - left + 1
        n2 = right - mid
        L = self.arr[left:mid + 1].copy()
        R = self.arr[mid + 1:right + 1].copy()

        i, j = 0, 0
        k = left
        colors = ['white'] * len(self.arr)

        # Highlight subarrays
        for idx in range(left, right + 1):
            colors[idx] = 'lightblue'
        self.states.append((self.arr.copy(), colors, "Merging subarrays [{}] to [{}]".format(left, right)))

        while i < n1 and j < n2:
            # Record comparison state
            colors[left + i] = 'yellow'  # Highlight left element
            colors[mid + 1 + j] = 'yellow'  # Highlight right element
            self.states.append((self.arr.copy(), colors, "Comparing {} and {}".format(L[i], R[j])))
            plt.pause(0.5)  # Simulated pause for detail

            if L[i] <= R[j]:
                self.arr[k] = L[i]
                i += 1
            else:
                self.arr[k] = R[j]
                j += 1
            colors[left + i - 1 if i > 0 else left] = 'green'  # Placed element
            colors[mid + 1 + j - 1 if j > 0 else mid + 1] = 'green'  # Placed element
            self.states.append((self.arr.copy(), colors, "Placed {} at position {}".format(self.arr[k], k)))
            k += 1
            colors[k - 1] = 'green'
            # Reset highlights
            colors[left + i] = 'lightblue' if i < n1 else 'white'
            colors[mid + 1 + j] = 'lightblue' if j < n2 else 'white'

        # Copy remaining elements
        while i < n1:
            self.arr[k] = L[i]
            colors[k] = 'green'
            self.states.append((self.arr.copy(), colors, "Copying remaining left: {}".format(L[i])))
            i += 1
            k += 1

        while j < n2:
            self.arr[k] = R[j]
            colors[k] = 'green'
            self.states.append((self.arr.copy(), colors, "Copying remaining right: {}".format(R[j])))
            j += 1
            k += 1

        # Final merged state
        self.states.append((self.arr.copy(), ['green' if idx >= left and idx <= right else 'white' for idx in range(len(self.arr))],
                            "Subarray [{}] to [{}] merged successfully".format(left, right)))

    def merge_sort_util(self, left, right):
        """
        Recursive utility for merge sort, recording divide states.
        :param left: Start index.
        :param right: End index.
        """
        colors = ['white'] * len(self.arr)
        if left < right:
            mid = (left + right) // 2

            # Highlight divide
            for idx in range(left, right + 1):
                colors[idx] = 'lightcoral'
            self.states.append((self.arr.copy(), colors, "Dividing array at mid = {}".format(mid)))

            # Recurse left
            self.merge_sort_util(left, mid)
            # Recurse right
            self.merge_sort_util(mid + 1, right)
            # Merge
            self.merge(left, mid, right)

    def generate_states(self):
        """
        Generate all animation states by performing merge sort.
        """
        # Initial state
        self.states.append((self.arr.copy(), ['white'] * len(self.arr), "Initial unsorted array: {}".format(self.arr)))
        self.merge_sort_util(0, len(self.arr) - 1)
        # Final sorted state
        self.states.append((self.arr.copy(), ['lightgreen'] * len(self.arr), "Merge Sort completed! Sorted array: {}".format(self.arr)))

    def create_animation(self):
        """
        Create and save the animation.
        """
        self.generate_states()
        fig, (ax, ax_text) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[3, 1])
        ax.set_xlim(0, len(self.arr) * self.width)
        ax.set_ylim(0, max(self.original_arr) * self.height_scale + 10)
        ax.set_title("Merge Sort Explainer", fontsize=16, fontweight='bold')
        ax.set_xlabel("Array Indices")
        ax.set_ylabel("Values")

        bars = ax.bar(range(len(self.arr)), self.arr, width=self.width, color='white', edgecolor='black')
        text_obj = ax_text.text(0.5, 0.5, "", ha='center', va='center', transform=ax_text.transAxes, fontsize=12, wrap=True)

        def animate(frame):
            arr_copy, colors, explanation = self.states[frame]
            # Update bars
            for i, (bar, height, color) in enumerate(zip(bars, arr_copy, colors)):
                bar.set_height(height)
                bar.set_color(color)
            # Update text
            text_obj.set_text(explanation)
            ax_text.set_xlim(0, 1)
            ax_text.set_ylim(0, 1)
            ax_text.axis('off')
            return bars + [text_obj]

        ani = animation.FuncAnimation(fig, animate, frames=len(self.states), interval=1500, blit=False, repeat=False)
        return ani

def main():
    """
    Main function to generate and save the Merge Sort explainer video.
    """
    animator = MergeSortAnimator(arr_size=8, max_value=20)  # Smaller array for clarity
    ani = animator.create_animation()

    output_dir = 'output'
    import os
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'merge_sort_explainer.mp4')
    ani.save(output_path, writer='ffmpeg', fps=1)  # Lower FPS for detailed steps
    plt.close()
    print(f"Merge Sort explainer video saved to {output_path}")
    print("The animation visualizes:")
    print("- Division of the array into subarrays (red highlights).")
    print("- Comparisons during merge (yellow highlights).")
    print("- Placement of elements (green highlights).")
    print("- Explanatory text for each step.")

if __name__ == "__main__":
    main()
