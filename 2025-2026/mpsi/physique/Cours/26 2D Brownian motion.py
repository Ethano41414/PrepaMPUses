import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


np.random.seed(5)


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)


def generateRandomLines(dt, N):
    
    dX = np.sqrt(dt) * np.random.randn(1, N)
    X = np.cumsum(dX, axis=1)
    
    dY = np.sqrt(dt) * np.random.randn(1, N)
    Y = np.cumsum(dY, axis=1)
    
    lineData = np.vstack((X, Y))
    
    return lineData


# Returns Line2D objects
def updateLines(num, dataLines, lines):
    for u, v in zip(lines, dataLines):
        u.set_data(v[0:2, :num])

    return lines


N = 501 # Number of points
T = 1.0
dt = T/(N-1)


fig, ax = plt.subplots()

data = [generateRandomLines(dt, N)]

ax = plt.axes(xlim=(-2.0, 2.0), ylim=(-2.0, 2.0))

## Uncomment for tight axes
##x = data[0][0]
##y = data[0][1]
##xmin = min(x)
##xmax = max(x)
##ymin = min(y)
##ymax = max(y)
##ax = plt.axes(xlim=(xmin+0.1*xmin, xmax+0.1*xmax), ylim=(ymin+0.1*ymin, ymax+0.1*ymax))

ax.set_xlabel('X(t)')
ax.set_ylabel('Y(t)')
#ax.set_title('2D Discretized Brownian Paths')

## Create a list of line2D objects
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1])[0] for dat in data]


## Create the animation object
anim = animation.FuncAnimation(fig, updateLines, N+1, fargs=(data, lines),
                                   interval=30, repeat=True, blit=True)

plt.tight_layout()
plt.show()

## Uncomment to save the animation
#anim.save('brownian2d_1path.mp4', writer=writer)
