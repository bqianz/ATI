from math import pi
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import StrMethodFormatter, NullFormatter

wavelength = 0.0555

incidence_angles_degree = np.array([30, 35, 40])

epsilon_degree = np.arange(0, 91);
cos_epsilon = np.cos(epsilon_degree / 180 * pi)

styles = ['-', '--', ':', '--']

for i, incidence_degree in enumerate(incidence_angles_degree):
    ratio = np.sin(incidence_degree / 180 * pi) * cos_epsilon
    label = r'$\theta_i$' + ' = {}'.format(incidence_degree) + r'$^\circ$'
    plt.plot(epsilon_degree, ratio, label=label, linestyle=styles[i], color='black')


plt.xlabel(r'$\varepsilon$' + ' [' + r'$^\circ$' + ']')
plt.ylabel(r'$ v_{tr} / v_{surf}$')
plt.legend()

plt.grid(b=True, which='major')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', alpha=0.2)

plt.show()
