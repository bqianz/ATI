from math import pi
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import StrMethodFormatter, NullFormatter

wavelength = 0.0555

incidence_degrees = np.arange(30, 40, 0.1)
epsilon_degrees = np.array([0, 30, 60, 90]);

styles = ['-', '--', ':', '-.']

for i, degree in enumerate(epsilon_degrees):
    ratio = np.sin(incidence_degrees / 180 * pi) * np.cos(degree / 180 * pi)
    label = r'$\varepsilon$' + ' = {}'.format(degree) + r'$^\circ$'
    plt.plot(incidence_degrees, ratio, label=label, linestyle=styles[i], color='black')


plt.xlabel(r'$\theta_i$' + ' [' + r'$^\circ$' + ']')
plt.ylabel(r'$ v_{tr} / v_{surf}$')
plt.legend(loc='lower right')

plt.grid(b=True, which='major')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', alpha=0.2)

plt.show()
