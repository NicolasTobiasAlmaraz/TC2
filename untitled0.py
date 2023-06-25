import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def plot_tf(tf, xlim=None):
    # Imprimo transferencia
    print(tf.num)
    print("----------------")
    print(tf.den)

    # Configurar los límites en el eje X si se proporcionan
    if xlim:
        w = np.logspace(np.log10(xlim[0]), np.log10(xlim[1]), num=1000)
    else:
        w = np.logspace(-2, 2, num=1000)

    # Calcular la respuesta en frecuencia
    w, mag, phase = signal.bode(tf, w)

    # Graficar la respuesta en módulo
    plt.figure()
    plt.semilogx(w, mag)
    plt.xlabel('Frecuencia [rad/s]')
    plt.ylabel('Magnitud [dB]')
    plt.title('Respuesta en Módulo')
    plt.grid(True)

    # Graficar la respuesta en fase
    plt.figure()
    plt.semilogx(w, phase)
    plt.xlabel('Frecuencia [rad/s]')
    plt.ylabel('Fase [grados]')
    plt.title('Respuesta en Fase')
    plt.grid(True)

    # Obtener los polos y ceros
    poles = tf.poles
    zeros = tf.zeros

    # Configuración del gráfico
    fig, ax = plt.subplots()
    ax.set_aspect('equal')  # Proporción de ejes igual para una circunferencia circular
    ax.axhline(0, color='gray', lw=0.5)  # Eje horizontal
    ax.axvline(0, color='gray', lw=0.5)  # Eje vertical
    ax.grid(True, linestyle='--', alpha=0.5)  # Activar la grilla

    # Traza la circunferencia unitaria
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    ax.plot(x, y, color='gray', linewidth=0.5, linestyle='--')

    # Traza los polos y ceros
    ax.plot(np.real(poles), np.imag(poles), 'x')
    ax.plot(np.real(zeros), np.imag(zeros), 'o')

    # Etiquetas y leyenda
    ax.set_xlabel('Parte real')
    ax.set_ylabel('Parte imaginaria')
    ax.set_title('Diagrama de polos y ceros', pad=10, loc='center')

    # Mostrar el gráfico
    plt.tight_layout()
    plt.show()


plt.close("all")

#Pasa Bajos
W0 = 1
WZ = 3
pInf = 1
Q = np.sqrt(2)/2
k=pInf/(WZ**2)
num = [1*k,0,k*WZ**2]
den1 = [1,W0/Q , W0**2]
den2 = [1,pInf]
den = np.polymul(den1, den2)
tf = signal.TransferFunction(num, den)
plot_tf(tf,xlim=[0.1,100])


#Pasa Altos
num1 = [1,0,1/9]
den1 = [1,np.sqrt(2),1]
num2 = [1,0]
den2 = [1,1]
num = np.polymul(num1, num2)
den = np.polymul(den1, den2)
tf = signal.TransferFunction(num, den)
plot_tf(tf,xlim=[0.001,100])
