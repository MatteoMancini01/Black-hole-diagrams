# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 00:21:20 2024

@author: mmanc
"""

import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from einsteinpy.coordinates import BoyerLindquistDifferential
from einsteinpy.metric import Kerr

# Metric or Black Hole parameters - Mass, M and Spin Parameter, a
sun_mass = 1.989e30 * u.kg
factor = 10
M = factor*sun_mass
a1 = 0.4 * u.one
a2 = 0.8 * u.one # Extremal Kerr Black Hole
a3 = 1* u.one
# Coordinate object to initialize metric with
# Note that, for this example
# the coordinate values below are irrelevant
bl = BoyerLindquistDifferential(
    t=0. * u.s,
    r=1e3 * u.m,
    theta=np.pi / 2 * u.rad,
    phi=np.pi * u.rad,
    v_r=0. * u.m / u.s,
    v_th=0. * u.rad / u.s,
    v_p=0. * u.rad / u.s,
)

# Defining two Kerr Black Holes, one with a higher spin parameter
kerr1 = Kerr(coords=bl, M=M, a=a1)
kerr2 = Kerr(coords=bl, M=M, a=a2)
kerr3 = Kerr(coords=bl, M=M, a=a3)

# Getting the list of singularities
sing_dict1 = kerr1.singularities()
sing_dict2 = kerr2.singularities()
sing_dict3 = kerr3.singularities()

# Sampling Polar Angle for plotting in Polar Coordinates
theta = np.linspace(0, 2 * np.pi, 100)

# Ergospheres
# These are functions
Ei1, Eo1 = sing_dict1["inner_ergosphere"], sing_dict1["outer_ergosphere"]
Ei2, Eo2 = sing_dict2["inner_ergosphere"], sing_dict2["outer_ergosphere"]
Ei3, Eo3 = sing_dict3["inner_ergosphere"], sing_dict3["outer_ergosphere"]

# Creating lists of points on Ergospheres for different polar angles, for both black holes
Ei1_list, Eo1_list = Ei1(theta), Eo1(theta)
Ei2_list, Eo2_list = Ei2(theta), Eo2(theta)
Ei3_list, Eo3_list = Ei3(theta), Eo3(theta)
# For Black Hole 1 (a = 0.4)
Xei1 = Ei1_list * np.sin(theta)
Yei1 = Ei1_list * np.cos(theta)

Xeo1 = Eo1_list * np.sin(theta)
Yeo1 = Eo1_list * np.cos(theta)

# For Black Hole 2 (a = 0.7)
Xei2 = Ei2_list * np.sin(theta)
Yei2 = Ei2_list * np.cos(theta)

Xeo2 = Eo2_list * np.sin(theta)
Yeo2 = Eo2_list * np.cos(theta)

# For Black Hole 3 (a = 1)
Xei3 = Ei3_list * np.sin(theta)
Yei3 = Ei3_list * np.cos(theta)

Xeo3 = Eo3_list * np.sin(theta)
Yeo3 = Eo3_list * np.cos(theta)

# Event Horizons
Hi1, Ho1 = sing_dict1["inner_horizon"], sing_dict1["outer_horizon"]
Hi2, Ho2 = sing_dict2["inner_horizon"], sing_dict2["outer_horizon"]
Hi3, Ho3 = sing_dict3["inner_horizon"], sing_dict3["outer_horizon"]

# For Black Hole 1 (a = 0.4)
Xhi1 = Hi1 * np.sin(theta)
Yhi1 = Hi1 * np.cos(theta)

Xho1 = Ho1 * np.sin(theta)
Yho1 = Ho1 * np.cos(theta)

# For Black Hole 2 (a = 0.7)
Xhi2 = Hi2 * np.sin(theta)
Yhi2 = Hi2 * np.cos(theta)

Xho2 = Ho2 * np.sin(theta)
Yho2 = Ho2 * np.cos(theta)

# For Black Hole 3 (a = 1)
Xhi3 = Hi3 * np.sin(theta)
Yhi3 = Hi3 * np.cos(theta)

Xho3 = Ho3 * np.sin(theta)
Yho3 = Ho3 * np.cos(theta)

fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(15,7.5), squeeze=True)

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.3)

# Adjust aspect ratio to make the plots square
ax1.set_aspect('equal')
ax2.set_aspect('equal')
ax3.set_aspect('equal')

size_plot = 4000*factor

ax1.fill(Xei1, Yei1, 'black', Xeo1, Yeo1, 'gray', Xhi1, Yhi1, 'black', Xho1, Yho1, 'gray', alpha=0.6, color = 'black')
ax1.set_title(f"$a = {a1}$", fontsize=18)
ax1.set_xlabel("X", fontsize=15)
ax1.set_ylabel("Y", fontsize=15)
ax1.set_xlim([-size_plot, size_plot])
ax1.set_ylim([-size_plot, size_plot])

ax2.fill(Xei2, Yei2, 'black', Xeo2, Yeo2, 'gray', Xhi2, Yhi2, 'black', Xho2, Yho2, 'gray', alpha=0.6, color = 'black')
ax2.set_title(f"$a = {a2}$", fontsize=18)
ax2.set_xlabel("X", fontsize=15)
ax2.set_ylabel("Y", fontsize=15)
ax2.set_xlim([-size_plot, size_plot])
ax2.set_ylim([-size_plot, size_plot])

ax3.fill(Xei3, Yei3, 'black', Xeo3, Yeo3, 'gray', Xhi3, Yhi3, 'black', Xho3, Yho3, 'gray', alpha=0.6, color = 'black')
ax3.set_title(f"$a = {a3}$", fontsize=18)
ax3.set_xlabel("X", fontsize=15)
ax3.set_ylabel("Y", fontsize=15)
ax3.set_xlim([-size_plot, size_plot])
ax3.set_ylim([-size_plot, size_plot])

horizon_o = mpatches.Patch(color='black', label='Outer horizon')
ergosphere1 = mpatches.Patch(color='dimgray', label='Ergosphere')

fig.legend(handles = [horizon_o, ergosphere1], loc='upper right', bbox_to_anchor=(1.0, 1), fontsize=12)

fig.suptitle(f"Black holes of mass $M = {factor}$ $M_\\odot$, for different values of the spin parameter a.")
