from math import pi
import numpy as np
import matplotlib.pyplot as plt

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
snr_dbs = np.arange(0,21,2)
snr_ratios = np.power(10, snr_dbs/10)
gamma_snrs = 1/(1+ 1/snr_ratios)
# gamma_snrs = np.arange(0.3, 1, 0.1)
gamma_snr_default = 0.76 # 5dB
gamma_quant = 0.99
gamma_amb = 0.96

# baselines = np.arange(40,160,20)
baselines = np.power(10, np.arange(0.7,3.4,0.02))
# baselines = np.arange(5,17,0.02)
baseline_default = 10

# baselines = np.arange(5,17)
baseline_default = 7.5

## number of looks
N1_default = 5041
N1s = np.array([5041,20165])

incidence_degrees = np.arange(30, 41, 2)
incidence_radians =  incidence_degrees * (180 / pi)
incidence_default = 35/180 * pi

plt.hlines(0.03,5,2000,color='c')
styles = ['-', '-.', ':', '--', '-']
# for angle in incidence_angles:
# for baseline in baselines:
# for angle in incidence_angles:
# for baseline in baselines:
# for gamma_snr in gamma_snrs
for i, wind_speed in enumerate(wind_speeds):

    ## coherence time
    t_c = 3.29 * wavelength / wind_speed

    # temporal baseline lag
    t_ati = baselines / (2 * v_orb)

    co_t = np.exp(-1 * np.square(t_ati) / np.square(t_c) )
    coherence = co_t * gamma_snr_default * gamma_amb * gamma_quant
    co_squared = np.square(coherence)

    phase_std = np.sqrt(np.divide(1 - co_squared,  2 * N1_default * co_squared))
    vrp_std = np.divide(phase_std * wavelength, np.sin(incidence_default) * 4 * pi*t_ati)

    label = r'$U$'+ ' = {} m/s'.format(wind_speed)
    # label='baseline = {}m'.format(baseline)
    #label='incidence angle = {} degrees'.format(incidence_angles)
    # label = 'SNR = {}dB'.format(snr)
    plt.loglog(baselines, vrp_std, linestyle = styles[i], color = 'black', label=label)

# plt.xlabel("SNR[dB]")
plt.xlabel(r'$B_{ATI}$'+' [m]')
# plt.xlabel("wind_speeds")
# plt.xscale('log')
# plt.xticks(baselines)
# plt.yscale('log')
plt.ylim((1E-3, 1))
plt.xlim((10**0.7, 2E3))

# plt.ylabel("Phase standard deviation[rad]")
plt.ylabel(r'$\sigma_{v_g}$'+ ' [m/s]')
plt.legend()

plt.grid(b=True, which='major')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', alpha=0.2)

plt.show()