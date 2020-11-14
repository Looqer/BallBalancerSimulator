import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation

from matplotlib.widgets import Slider, Button, RadioButtons

plt.rcParams["figure.figsize"] = 8, 10


x = 0
y = 0
xv = 0
yv = 0
xa = 0.00005
ya = 0.0001

delta = 0.00001

# create a figure with an axes
fig, ax = plt.subplots()

# set the axes limits
ax.axis([-1.6, 1.6, -1.6, 1.6])

# create a point in the axes
point, = ax.plot(0, 1, marker="o")

plt.subplots_adjust(left=0.1, bottom=0.3)

axcolor = 'lightgoldenrodyellow'
axx = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor=axcolor)
axy = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor=axcolor)

sx = Slider(axx, 'xa', -0.0001, 0.0001, valinit=0, valstep=delta)
sy = Slider(axy, 'ya', -0.0001, 0.0001, valinit=0, valstep=delta)


# Updating function, to be repeatedly called by the animation


def update(i):
    global x, y, xv, yv
    oldx = []
    oldy = []
    # obtain point coordinates
    oldx.append(x)
    oldy.append(y)

    if (abs(x) >= 1.5):
        xv = -xv

    x = x + xv
    xv = xv + sx.val
    if (xv < 0):
        xv = xv + 0.000009
    elif (xv > 0):
        xv = xv - 0.000009
    else:
        xv = xv

    if (abs(y) >= 1.5):
        yv = -yv

    y = y + yv
    yv = yv + sy.val
    if (yv < 0):
        yv = yv + 0.000009
    elif (yv > 0):
        yv = yv - 0.000009
    else:
        yv = yv

    #plt.plot(x,y)
    plt.plot(oldx, oldy)
    # set point's coordinates
    point.set_data([oldx], [oldy])
    
    return point,

# create animation with 10ms interval, which is repeated

ani = FuncAnimation(plt.gcf(), update, interval=10, blit = True, repeat = False)

plt.show()
