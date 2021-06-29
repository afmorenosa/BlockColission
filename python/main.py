"""."""
from matplotlib import pyplot as plt
from matplotlib import animation
from system import system

fig = plt.figure()
ax = plt.axes(xlim=(0, 20), ylim=(0, 1))

my_system = system.simple_system()
line, = ax.plot([], [], "bo")
line2, = ax.plot([], [], "ro")
coll_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

nframes = 500


def init():
    """Set data for animation."""
    line.set_data([], [])
    line2.set_data([], [])
    coll_text.set_text('')

    return line, line2, coll_text


def animate(i):
    """Update animation."""
    for j in range(100):
        my_system.time_step_evolution()

    x_1 = [my_system.box_1.x]
    y_1 = [0.5]

    x_2 = [my_system.box_2.x]
    y_2 = [0.5]

    charged = "=" * int(60 * (i + 1) / nframes - 1)
    uncarged = " " * (60 - int(60 * (i + 1) / nframes - 1) - 1)

    print("[" + charged + ">" + uncarged + "] Rendering...", end='\r')

    line.set_data(x_1, y_1)
    line2.set_data(x_2, y_2)
    coll_text.set_text(f"n collisions={my_system.coll_counter}")

    return line, line2, coll_text


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nframes, interval=10, blit=True)

# Save animation
anim.save('Fourier.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

print()
