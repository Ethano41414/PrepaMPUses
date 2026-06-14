import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from matplotlib import animation

# Define constants
N = 1024  # Number of points
L = 100.0  # Length of the domain
dx = L / N  # Spatial step size
x = np.linspace(-L/2, L/2, N)  # Spatial grid

# Initial wave packet parameters
x0 = -35.0  # Initial position
k0 = 2.50  # Initial wave number
sigma = 1.0  # Width of the wave packet

# Initial wave packet
psi0 = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
psi0 /= np.sqrt(np.sum(np.abs(psi0)**2))  # Normalize

# Time evolution parameters
dt = 0.01  # Time step
t_max = 14.0  # Maximum time
t = np.arange(0, t_max, dt)

# Fourier space
k = 2 * np.pi * np.fft.fftfreq(N, d=dx)

# Time evolution
psi = psi0.copy()
psi_t = [psi0]

for _ in t:
    psi_k = fft(psi)
    psi_k *= np.exp(-1j * k**2 * dt / 2)
    psi = ifft(psi_k)
    psi_t.append(psi)

# Animation
fig, ax = plt.subplots(figsize=(10,4))
ax.grid()
line1, = ax.plot(x, np.abs(psi0),'--', color='orange')
line2, = ax.plot(x, -np.abs(psi0),'--', color = 'orange')
line3, = ax.plot(x, np.imag(psi0), color='blue')

def animate(i):
    line1.set_ydata(np.abs(psi_t[i]))
    line2.set_ydata(-np.abs(psi_t[i]))
    line3.set_ydata(np.imag(psi_t[i]))
    fig.tight_layout()
    if not (i % 200) :
        fig.savefig('frame_dispersion_{:03d}.png'.format(i//200), dpi = 600)
    return line1, line2, line3

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=10, repeat = False)
ani.save('Dispersion_wave_packet.mp4', fps=30)
plt.show()
