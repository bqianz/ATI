from math import pi
import numpy as np
import matplotlib.pyplot as plt


v_orb = 7545 # ECEF Velocity
wavelength = 0.0555

baseline = 7.5

# incidence_degrees = np.power(10, np.arange(1.47, 1.61, 0.01))
incidence_degrees = np.arange(30, 40.1, 0.01)
incidence_radians =  incidence_degrees / 180 * pi
current_velocities = np.array([0.1, 0.5, 1, 3])

styles = ['-.', '-', ':', '--', '-']
# for degree in incidence_degrees:
for i, cur_vel in enumerate(current_velocities):
    phase = 2 * pi * baseline * np.sin(incidence_radians) * cur_vel/ (wavelength*v_orb)
    phase_deg = phase / pi * 180

    label = r'$v_{surf}$' + ' = {} m/s'.format(cur_vel)
    plt.plot(incidence_degrees, phase_deg, label=label, linestyle=styles[i], color='black')

plt.xlabel(r'$\vartheta$' + ' [' + r'$^\circ$' + ']')
plt.ylabel('ATI phase ' + r'$\varphi_{ATI}$' + ' [' + r'$^\circ$' + ']')
plt.xlim(30, 40)
plt.legend()
plt.grid(b=True, which='major')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', alpha=0.2)
plt.show()