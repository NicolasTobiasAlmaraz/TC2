import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.close("all")

# Levanto .CSV en DataFrames
data_vo_vi = pd.read_csv('MedicionesModulo.csv', delimiter=';')
data_fase = pd.read_csv('MedicionesFase.csv', delimiter=';')

# Leo para rta en modulo
frequencies_vo_vi = data_vo_vi['F']
vi = data_vo_vi['Vi']
vo = data_vo_vi['Vo']

# Leo para rta en fase
frequencies_fase = data_fase['F']
delta_t = data_fase['deltaT']

# Calculo rta en modulo
vo_vi = 20*np.log(vo / vi)

# Calculo rta en fase
desfasaje = 2 * np.pi * frequencies_fase * delta_t

# Calcular la derivada del desfasaje respecto a la frecuencia
derivada_desfasaje = np.gradient(desfasaje, frequencies_fase)*1000

# Hago figura con 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

# Subplot 1: Curva Modulo
ax1.semilogx(frequencies_vo_vi, vo_vi)
ax1.set_ylabel('|T| [dB]')
ax1.set_title('Respuesta en frecuencia')
ax1.grid(True)

# Subplot 2: Curva Fase
ax2.semilogx(frequencies_fase, desfasaje)
ax2.set_ylabel('fi [rad]')
ax2.grid(True)

# Subplot 3: Retardo de Grupo
ax3.semilogx(frequencies_fase, derivada_desfasaje)
ax3.set_xlabel('F [Hz]')
ax3.set_ylabel('Ret Gru [ms]')
ax3.grid(True)

# Ajustar la disposición de los subplots
plt.tight_layout()

# Mostrar la gráfica
plt.show()