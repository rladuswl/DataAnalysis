import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 3, 1) # sin
a = np.linspace(-10, 10)
plt.plot(np.sin(a), 'r--', lw=1)

plt.subplot(1, 3, 2) # cos
b = np.linspace(-10, 10)
plt.plot(np.cos(b), 'b-', lw=1)

plt.subplot(1, 3, 3) # sin + cos
c = np.linspace(-10, 10)
plt.plot(np.sin(c), 'g--')
plt.plot(np.cos(c), 'g--')