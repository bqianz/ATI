from math import pi
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import StrMethodFormatter, NullFormatter

# dtart ~ 0.04
# N_s = 3 # number of sub swaths?
antenna_length = 15
wavelength = 0.0555

# v_orb = 7453 # from mean orbit altitude 798km
v_orb = 7545 # ECEF Velocity

wind_speed_default = 2.5
wind_speeds = np.array([3,6,9,12,15])

## snr coherence
# snrs = np.arange(3,20)
# snr_default = 5
snr_dbs = np.arange(0,21,0.05)
snr_ratios = np.power(10, snr_dbs/10)
gamma_snrs = 1/(1+ 1/snr_ratios)
# gamma_snrs = np.arange(0.3, 1, 0.1)
gamma_snr_default = 0.76 # 5dB

gamma_amb = 0.96

# baselines = np.power(10, np.arange(0.7,3.3,0.02))

baselines = np.arange(5,17,0.02)
baseline_default = 10

## number of looks
N1_default = 5041
N1s = np.array([5041,20165])

incidence_degrees = np.arange(30, 41, 2)
incidence_radians =  incidence_degrees * (180 / pi)
incidence_default = 35/180 * pi

for degree in incidence_degrees:
# for baseline in baselines:
# for snr in snr_dbs:
# for wind_speed in wind_speeds:

    rad = degree/180 * pi
    # gamma_snr = 1/(1+ 1/10**(snr/10))
    ## coherence time
    t_c = 3.29 * wavelength / wind_speed_default

    # temporal baseline lag
    t_ati = baseline_default / (2 * v_orb)

    co_t = np.exp(-1 * np.square(t_ati) / np.square(t_c) )
    coherence = co_t * gamma_snrs * gamma_amb
    co_squared = np.square(coherence)

    phase_std = np.sqrt(np.divide(1 - co_squared,  2 * N1_default * co_squared))
    vrp_std = np.divide(phase_std * wavelength, np.sin(rad) * 4 * pi*t_ati)

    # label = "ws = {}m/s".format(wind_speed)
    # label='baseline = {}m'.format(baseline)
    label=r'$\theta_i$' + ' = {}'.format(degree) + r'$^\circ$'
    # label = 'SNR = {} dB'.format(snr)
    
    plt.plot(snr_dbs, phase_std, label=label)

ax = plt.gca()

plt.xlabel("SNR[dB]")
# plt.xlabel("baseline[m]")
# plt.xlabel("wind_speeds")
# plt.xscale('log')
# plt.xticks(baselines)
# plt.yscale('log')

# plt.ticklabel_format(axis='y', style='plain')

ax.yaxis.set_major_formatter(StrMethodFormatter('{x:.3f}'))
# ax.yaxis.set_minor_formatter(StrMethodFormatter('{x:.2f}'))

# plt.ylim((1E-2, 1))

plt.ylabel("Phase standard deviation[rad]")
# plt.ylabel("Velocity standard deviation[m/s]")
plt.legend()

plt.grid(b=True, which='major')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', alpha=0.2)

# plt.savefig('phase_std.png')
plt.show()
