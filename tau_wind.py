from math import pi
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import StrMethodFormatter, NullFormatter

wavelength = 0.0555

# wind_speeds = np.array([3, 6, 9, 12, 15])
wind_speeds = np.arange(2, 16, 0.1)
tau_c = 3.29 * wavelength / wind_speeds;

plt.plot(wind_speeds, tau_c, 'k-')
plt.xlabel("Wind speed [m/s]")
plt.ylabel("Coherence time [s]")
plt.show()
