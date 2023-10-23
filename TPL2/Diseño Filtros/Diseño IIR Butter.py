# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 19:29:11 2023

@author: guido
"""
import scipy.signal as sig
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio
import pytc2.sistemas_lineales as tc2

plt.close("all")
fs = 44100 # Hz
nyq_frec = fs / 2
ripple = 1 # dB
atenuacion = 20 # dB

ws1 = 3000 #Hz
wp1 = 2000 #Hz


##################################################################
#### Modifico las SOS para que ninguna atenue mucho en la banda de paso
##################################################################
lp_sos_butter = sig.iirdesign(wp = wp1/nyq_frec, ws = ws1/nyq_frec, gpass = ripple, gstop = atenuacion, analog=False, ftype='butter', output='sos')      

frecuencias = np.linspace(0, 22050, num = 10000)

#plt.figure(figsize=(10, 4))  


ganancia_bp = 0 # En db
mult =( 10**(ganancia_bp/4 / 20) ) 

lp_sos_butter[0, 0 : 3 ] = lp_sos_butter[0, 0 : 3] *  1e5 * mult   

lp_sos_butter[1, 0 : 3 ] = lp_sos_butter[1, 0 : 3] *  2e-2 * mult  

lp_sos_butter[2, 0 : 3 ] = lp_sos_butter[2, 0 : 3] * 0.25e-1 * mult

lp_sos_butter[3, 0 : 3 ] = lp_sos_butter[3, 0 : 3] * 2e-2   *mult 

_, h1 = sig.sosfreqz(lp_sos_butter[0, :], frecuencias, fs = fs)
_, h2 = sig.sosfreqz(lp_sos_butter[1, :], frecuencias, fs = fs)
_, h3 = sig.sosfreqz(lp_sos_butter[2, :], frecuencias, fs = fs)
_, h4 = sig.sosfreqz(lp_sos_butter[3, :], frecuencias, fs = fs)
w, h = sig.sosfreqz(lp_sos_butter, frecuencias, fs = fs)
#plt.title('Respuesta en modulo IIR separadas')
#plt.plot(w, 20 * np.log10(np.abs(h)),label = "Transferencia")
#plt.plot(w, 20 * np.log10(np.abs(h1)),label = "SOS 1")
#plt.plot(w, 20 * np.log10(np.abs(h2)),label = "SOS 2")
#plt.plot(w, 20 * np.log10(np.abs(h3)),label = "SOS 3")
#plt.plot(w, 20 * np.log10(np.abs(h4)),label = "SOS 4")
#plt.ylabel('Amplitude [dB]')
#plt.xlabel('Frequency [Hz]')
#plt.legend()
#plt.grid()
#plt.show()

#Calculo rta mod y fase
moduloIIR = 20*np.log10(abs(h))
faseIIR = np.angle(h)*180/np.pi

ejeMuestrasIIR = w*(2*np.pi/fs)
retardoGrupoIIR = -np.diff(faseIIR) / np.diff(ejeMuestrasIIR)

#Respuesta en modulo
plt.figure(1)
plt.plot(w, moduloIIR)
plt.title('Respuesta en Módulo')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('|H(z)| [dB]')
plt.grid()
#tc2.plot_plantilla(filter_type = 'lowpass', fpass = [wp1], ripple = ripple, fstop = ws1, attenuation = atenuacion, fs = fs)
plt.show()

#Respuesta en fase
plt.figure(2)
plt.plot(w, faseIIR)
plt.title('Respuesta en Fase')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('φ{H(z)} [°]')
plt.grid()
plt.show()

#Ret grupo
plt.figure(3)
plt.plot(w[:-1], retardoGrupoIIR)
plt.title('Retardo de grupo')
plt.xlabel('Frecuencia discreta [Hz]')
plt.ylabel('Retardo de grupo [muestras]')
plt.grid()
plt.show()

#print coeficientes b
print("                  Numerador           |                Denominador         ")
print(lp_sos_butter)