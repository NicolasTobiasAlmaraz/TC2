# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 18:19:49 2023

@author: User
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np

# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

w0 = 1*10
q = 1/np.sqrt(2)

plt.close('all')

my_tf = TransferFunction( [w0**2], [1, w0/q, w0**2])    

bodePlot(my_tf, fig_id=1, filter_description = 'Q={:3.3f}'.format(q) )
pzmap(my_tf, fig_id=2, filter_description = 'Q={:3.3f}'.format(q)) #S plane pole/zero plot
