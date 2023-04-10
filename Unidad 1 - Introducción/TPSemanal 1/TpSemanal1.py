"""
TP Semanal 1
Nicolás Almaraz

Pasatodo 1er Orden
Transferencia Normalizada
"""

from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
from pytc2.sistemas_lineales import pzmap, bodePlot

my_tf = TransferFunction( [1, -1], [1, 1])

plt.close('all')

bodePlot(my_tf, fig_id=1 )
pzmap(my_tf, fig_id=2 )
