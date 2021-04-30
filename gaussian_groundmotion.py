import numpy as np
import matplotlib.pyplot as plt

# Initialize
n = 1000
mint = 0
maxt = 5
dt = (maxt-mint)/n
fdom = 5
tdom = 2.5
a = 1./tdom
t = np.linspace(mint,maxt,num=n)

# Original gaussian function for source time function
fori = (a) * np.exp(-1 * ((t-tdom)**2 / a**2))

# First derivative of gaussian function for source time function
fraw = (-2 * (t-tdom) / a) * np.exp(-1 * ((t - tdom)**2 / a**2))

# Plot
plt.plot(t,fraw,label='f`(t)')
plt.plot(t,fori,label='f(t)')
plt.legend()
plt.grid()
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Gaussian Source Time Function')
plt.show()