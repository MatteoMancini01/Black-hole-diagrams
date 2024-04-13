# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:46:20 2024

@author: mmanc
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Rs = 2

def ergosphere(r, a, theta):
    return (Rs + np.sqrt(Rs**2 - 4*a**2*np.cos(theta)**2))/2
def horizon(r, a):
    return (r + np.sqrt(r**2 - 4*a**3))/2

def kerr_black_hole(a):
    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2*np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    r_bh = horizon(Rs, a)
    r_ergo = ergosphere(Rs, a, phi)
    
    # Convert spherical coordinates to Cartesian coordinates
    x_ergo = r_ergo * np.sin(theta) * np.cos(phi)
    y_ergo = r_ergo * np.sin(theta) * np.sin(phi)
    z_ergo = r_ergo * np.cos(theta)
    
    x_bh = r_bh * np.sin(theta) * np.cos(phi)
    y_bh = r_bh * np.sin(theta) * np.sin(phi)
    z_bh = r_bh * np.cos(theta)
    
    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot ergosphere
    ax.plot_surface(x_ergo, y_ergo, z_ergo, color='gray', alpha=0.5)
    ax.plot([], [], [], 'o',color = 'gray', label='Ergosphere', alpha = 0.5)
    # Plot event horizon
    ax.plot_surface(x_bh, y_bh, z_bh, color='black', alpha = 0.8)
    ax.plot([], [], [], 'ko', label='Outer horizon', alpha = 0.8)
    
    
    ax.set_xlabel(r'$\frac{X}{R_s}$')
    ax.set_ylabel(r'$\frac{Y}{R_s}$')
    ax.set_zlabel(r'$\frac{Z}{R_s}$')
    ax.set_title(f'Kerr Black Hole (a={a})')
    ax.legend()
    plt.show()

# Example usage
a = 0.99  # Spin parameter
kerr_black_hole(a)
#%%




