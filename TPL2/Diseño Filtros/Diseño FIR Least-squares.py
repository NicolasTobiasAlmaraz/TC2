# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:41:33 2023

@author: guido
"""

import numpy as np

from scipy.signal import firls, freqz
import matplotlib.pyplot as plt
import pytc2.sistemas_lineales as tc2
plt.close("all")

# Especifica las características del filtro
fs = 44100 # Hz
nyq_frec = fs / 2
FPB1 = 2e3
FPB2 = 8e3
FSB1 = 4e3
FSB2 = 6e3

# Diseña el filtro FIR utilizando el método de mínimos cuadrados

orden_del_filtro = 71

desp_fc = 550 # para reducir el orden del filtro desplazo las bandas de paso para que no atenuen en los extremos

bandas = [0,FPB1 + desp_fc ,FPB1 + desp_fc,FPB2 - desp_fc,FPB2 - desp_fc,nyq_frec]
atenuaciones = [1,1,0,0,1,1]

num = firls(numtaps=orden_del_filtro, bands= bandas, desired=atenuaciones, fs=fs)

w, h = freqz( num )

# renormalizo el eje de frecuencia

w = w / np.pi * nyq_frec

#####################
#Calculo respuesta en modulo fase y retardo grupo
#####################
moduloFIR = 20*np.log10(abs(h))

faseFIR = np.angle(h)*180/np.pi

ejeMuestrasFIR = w*(2*np.pi/fs)
retardoGrupoFIR = -np.diff(faseFIR) / np.diff(ejeMuestrasFIR)

#Plot modulo
plt.figure(1)
plt.plot(w, moduloFIR)
plt.title('Respuesta en Módulo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|H(z)| [dB]')
plt.grid()
tc2.plot_plantilla(filter_type = 'bandstop', fpass = [FPB1,FPB2], ripple = 1, fstop = [FSB1,FSB2], attenuation = 20, fs = fs)
plt.show()

#plot fase
plt.figure(2)
plt.plot(w, faseFIR)
plt.title('Respuesta en Fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('φ{H(z)} [°]')
plt.grid()
plt.show()

#plot ret grupo
plt.figure(3)
plt.plot(w[:-1], retardoGrupoFIR)
plt.title('Retardo de grupo')
plt.xlabel('Frecuencia discreta [Hz]')
plt.ylabel('Retardo de grupo [muestras]')
plt.grid()
plt.show()


#Imprimo coeficientes
np.set_printoptions(precision=10, suppress=True)
num_str = ', '.join(map(str, num))
print("[" + num_str + "]")