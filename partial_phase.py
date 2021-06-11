from math import pi
import numpy as np
import matplotlib.pyplot as plt


v_orb = 7545 # ECEF Velocity
wavelength = 0.0555

baselines = [2.5, 5, 7.5, 10]

# incidence_degrees = np.power(10, np.arange(1.47, 1.61, 0.01))
incidence_degrees = np.arange(30, 41, 0.02)
incidence_radians =  incidence_degrees / 180 * pi

styles = ['-.', ':', '-', '--']
widths = [1, 1, 3, 1]
# for degree in incidence_degrees:
for i, baseline in enumerate(baselines):
    d_phase = 2* pi * baseline * np.sin(incidence_radians) / (wavelength*v_orb)
    d_phase = d_phase / pi * 180

    label = r'$B_{ATI}$' + ' = {} m'.format(baseline)
    if baseline==7.5:
        label += ' (RS2)'
    plt.plot(incidence_degrees, d_phase, label=label, linestyle=styles[i], linewidth = widths[i], color='black')

plt.xlabel("Incidence angle [deg]")
# plt.ylabel(r'$\frac{\partial}{\partial v_g} \varphi_{ATI}$' + ' [rad' + r'$\cdot$' + 's/m]')
plt.ylabel(r'$\partial \varphi_{ATI} / \partial v_g$' + ' [deg' + r'$\cdot$' + 's/m]')
# plt.ylabel(r'$\frac{\partial}{\partial v_g} \varphi_{ATI}$' + r'\mbox{\Large\( % [rad s/m]%\)}')
# plt.ylabel('Partial derivative of ATI phase w.r.t ground velocity [rad s/m]')
plt.xlim(30,40)
# plt.ylim(0.03, 0.15)
plt.legend()
plt.show()