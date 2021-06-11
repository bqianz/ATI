from math import pi
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import StrMethodFormatter, NullFormatter

# colors = ['blue', 'orange', 'green', 'red']

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
gamma_quant = 0.99

gamma_amb = 0.96

# baselines = np.power(10, np.arange(0.7,3.3,0.02))

# baselines = np.arange(5,17,0.02)
baselines = [2.5, 5, 7.5, 10]
# baselines = np.arange(5,17,2)
baseline_default = 7.5

## number of looks
N1_default = 5041
N2_default = 20165
N1s = np.array([5041,20165])

# incidence_degrees = np.arange(30, 41, 2)
incidence_degrees = np.arange(30, 41, 0.02)
incidence_radians =  incidence_degrees * (180 / pi)
incidence_default = 35/180 * pi

plt.hlines(0.1,0,20,color='c')

styles = [':', '-.', '-', '--']
widths = [1, 1, 3, 1]

for i, baseline in enumerate(baselines):
# for snr in snr_dbs:
# for wind_speed in wind_speeds:

    # gamma_snr = 1/(1+ 1/10**(snr/10))
    ## coherence time
    t_c = 3.29 * wavelength / wind_speed_default

    # temporal baseline lag
    t_ati = baseline / (2 * v_orb)

    co_t = np.exp(-1 * np.square(t_ati) / np.square(t_c) )
    coherence = co_t * gamma_snrs * gamma_amb * gamma_quant
    co_squared = np.square(coherence)

    phase_std = np.sqrt(np.divide(1 - co_squared,  2 * N2_default * co_squared))
    vrp_std = np.divide(phase_std * wavelength, np.sin(incidence_default) * 4 * pi*t_ati)
        
    
    # label=r'$\theta_i$' + ' = {}'.format(degree) + r'$^\circ$'
    # label = 'SNR = {} dB'.format(snr)
    
    plt.semilogy(snr_dbs, vrp_std, color = 'r', linestyle=styles[i], linewidth=widths[i])

for i, baseline in enumerate(baselines):

    # gamma_snr = 1/(1+ 1/10**(snr/10))
    ## coherence time
    t_c = 3.29 * wavelength / wind_speed_default

    # temporal baseline lag
    t_ati = baseline / (2 * v_orb)

    co_t = np.exp(-1 * np.square(t_ati) / np.square(t_c) )
    coherence = co_t * gamma_snrs * gamma_amb * gamma_quant
    co_squared = np.square(coherence)
    

    phase_std = np.sqrt(np.divide(1 - co_squared,  2 * N1_default * co_squared))
    vrp_std = np.divide(phase_std * wavelength, np.sin(incidence_default) * 4 * pi*t_ati)

    # label = "ws = {}m/s".format(wind_speed)
    # label='B = {}m'.format(baseline)
    # label=r'$\theta_i$' + ' = {}'.format(degree) + r'$^\circ$'
    # label = 'SNR = {} dB'.format(snr)
    
    label= r'$B_{ATI}$'+' = {} m'.format(baseline)

    if baseline==7.5:
        label += ' (RS2)'

    plt.semilogy(snr_dbs, vrp_std, color = 'black', linestyle=styles[i], linewidth=widths[i], label=label)

for i, baseline in enumerate(baselines):
# for snr in snr_dbs:
# for wind_speed in wind_speeds:

    # gamma_snr = 1/(1+ 1/10**(snr/10))
    ## coherence time
    t_c = 3.29 * wavelength / wind_speed_default

    # temporal baseline lag
    t_ati = baseline / (2 * v_orb)

    co_t = np.exp(-1 * np.square(t_ati) / np.square(t_c) )
    coherence = co_t * gamma_snrs * gamma_amb * gamma_quant
    co_squared = np.square(coherence)

    phase_std = np.sqrt(np.divide(1 - co_squared,  2 * N2_default * co_squared))
    vrp_std = np.divide(phase_std * wavelength, np.sin(incidence_default) * 4 * pi*t_ati)
        
    
    # label=r'$\theta_i$' + ' = {}'.format(degree) + r'$^\circ$'
    # label = 'SNR = {} dB'.format(snr)
    
    plt.semilogy(snr_dbs, vrp_std, color = 'r', linestyle=styles[i], linewidth=widths[i])


ax = plt.gca()

plt.xlabel("SNR [dB]")
# plt.xlabel("baseline[m]")
# plt.xlabel("wind_speeds")
# plt.xlabel("Incidence angle[deg]")
# plt.xscale('log')
# plt.xticks(baselines)
# plt.yscale('log')

# plt.ticklabel_format(axis='y', style='plain')

ax.set_yticks([0.02,0.03,0.05,0.1,0.2,0.3,0.5])
ax.yaxis.set_major_formatter(StrMethodFormatter('{x:.2f}'))
# ax.yaxis.set_minor_formatter(StrMethodFormatter('{x:.2f}'))

# plt.ylim((0.02, 0.5))
plt.xlim((0,20))

# plt.ylabel("Phase standard deviation[rad]")
plt.ylabel(r'$\sigma_{v_g}$'+ ' [m/s]')
# ax.yaxis.get_ticklabels()[2].set_visible(False)

plt.legend()

plt.grid(b=True, which='major')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', alpha=0.2)

# plt.savefig('phase_std.png')
plt.show()
