import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
mpl.rcParams['font.size'] = 14

def F(x):
    return ((x - 0.1)**3) * ((x - 0.5)**2) * ((x - 0.95)**1) * (1 / (0.03 + x**2))


# Set initial interval and midpoint
a = 0.85
b = 1.0
c = (a + b) / 2.0

a_plot = a - 0.05
b_plot = b + 0.05

# Plot F(x) over [a_plot, b_plot]
x = np.linspace(a_plot, b_plot, 10001)
fig, ax = plt.subplots(figsize=(15, 8))
ax.axhline(0.0, color = "#888888")
ax.plot(x, F(x), color = "k", linestyle = "-")
ax.set(xlabel=r"$x$", ylabel=r"$F(x)$")
ax.set_xlim([a_plot, b_plot])

# Draw a blue line at the midpoint, and red lines for interval bounds
ax.axvline(a, color = "#ff0000")
ax.axvline(b, color = "#ff0000")

ax.axvline(c, color = "#0000ff")
ax.plot(c, 0, 'o', color = "#0000ff")

# Turn on "interactive plotting", show the figure,
# pause for 2 seconds
plt.ion()
plt.show()
plt.pause(2)

for i in range(1, 6):
    
    # Bisection iteration
    if F(a) * F(c) <= 0.0:
        b = c
    else:
        a = c
    
    # Clear axes
    ax.clear()
    
    # Find new midpoint and plot again
    c = (a + b) / 2.0

    # The figure will update automatically thanks to plt.ion()
    ax.axhline(0.0, color = "#888888")
    ax.plot(x, F(x), color = "k", linestyle = "-")
    ax.axvline(a, color = "#ff0000")
    ax.axvline(b, color = "#ff0000")

    ax.axvline(c, color = "#0000ff")
    ax.plot(c, 0, 'o', color = "#0000ff")
    
    ax.set(xlabel=r"$x$", ylabel=r"$F(x)$")
    ax.set_xlim([a_plot, b_plot])
    
    # Pause for 2 seconds to see the new plot
    plt.pause(2)
    
plt.pause(5)