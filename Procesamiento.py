# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:51:00 2024

@author: valen
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:22:12 2024

@author: valen
"""

import  wfdb
import matplotlib.pyplot as plt
import numpy as np

N = 1950
x = np.random.randn(N)


signal= wfdb.rdrecord ('C:/Users/valen/Downloads/charis9')
valores = signal.p_signal
indice_seleccionado = 2
valores = signal.p_signal[:, indice_seleccionado]
valoresr = valores.flatten()[:1950]

# Calcular la media de los valores reducidos
media = np.mean(valoresr)
print(f"Media : {media}")
# Calcular la desviación estándar de los valoresr
desviacion = np.std(valoresr)
print(f"Desviación: {desviacion}")
#coeficiente de variacion
coeficiente=(desviacion/media)*100
print(f"Coeficiente: {coeficiente}")

# RUIDO GAUSSIANO
escala_ruido = 0.7
ruido_gaussiano = escala_ruido * np.random.randn(len(valoresr))

# RUIDO IMPULSO
desviacion_estandar_ruido_impulso = 0.1
ruido_impulso = np.random.normal(0, desviacion_estandar_ruido_impulso, len(valoresr))
ruido_impulso[ruido_impulso < 0.05] = 0

# Señal contaminada con ruido gaussiano y ruido impulsivo
signalruido = valoresr + ruido_gaussiano + ruido_impulso

# Generar ruido artefacto
ruido_artefacto = np.random.normal(0, 0.5, len(valoresr))  # ajusta la desviación estándar según sea necesario

# Contaminar la señal con ruido artefacto
signal_ruido_artefacto = valoresr + ruido_artefacto

# Potencia de la señal original
P_signal = np.mean(valoresr ** 2)

# Potencia del ruido artefacto
P_noise_artefacto = np.mean(ruido_artefacto ** 2)

# Calcular SNR de la señal con ruido artefacto
SNR_artefacto = 10 * np.log10(P_signal / P_noise_artefacto)

# Imprimir el resultado
print("SNR del ruido artefacto:", SNR_artefacto, "dB")


# Potencia de la señal original
P_signal = np.mean(valoresr ** 2)

# Potencia del ruido impulsivo
P_noise = np.mean(ruido_impulso ** 2)

# Calcular SNR IMPULSO
SNR_impulso= 10 * np.log10(P_signal / P_noise)
print("SNR señal impulso:", SNR_impulso, "dB")

# Potencia de la señal y del ruido
potencia_senial = np.mean(valoresr**2)
potencia_ruido = np.mean((ruido_gaussiano + ruido_impulso)**2)

#  SNR 
SNR_dB = 10 * np.log10(potencia_senial / potencia_ruido)
print(f"SNR : {SNR_dB:.2f} dB")


# Graficar la señal original
plt.figure()
plt.plot(valoresr)
plt.title('Señal Original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()

# Graficar la señal original
plt.figure()
plt.hist(valoresr)
plt.title('Histograma de la Señal Original')
plt.xlabel('Amplitud')
plt.ylabel('Frecuencia')
plt.show()

# Graficar la señal contaminada con ruido
plt.figure()
plt.plot(signalruido, color='orange')
plt.title('Señal con Ruido')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()

# Graficar el ruido gaussiano
plt.figure()
plt.plot(ruido_gaussiano, color='red')
plt.title('Ruido Gaussiano')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()

# Graficar el ruido impulsivo
plt.figure()
plt.plot(ruido_impulso, color='green')
plt.title('Ruido Impulso')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()

# Graficar la señal contaminada con ruido artefacto
plt.plot(signal_ruido_artefacto)
plt.title("Señal con Ruido Artefacto")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.show()

