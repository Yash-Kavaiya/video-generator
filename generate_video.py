import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os

# Parameters for the animation
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # Update the data
    return line,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Save as MP4 (requires ffmpeg; handled in GitHub Actions environment)
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, 'sine_wave_animation.mp4')
ani.save(output_path, writer='ffmpeg', fps=20)

print(f"Video saved to {output_path}")
