# -*- coding: utf-8 -*-

import wfdb
import matplotlib.pyplot as plt
import random
import math

N = 1950
signal = wfdb.rdrecord('C:/Users/valen/Downloads/charis9')
valores = signal.p_signal
indice_seleccionado = 2
valores = signal.p_signal[:, indice_seleccionado]
valoresr = valores.flatten()[:1950]

# Calcular la media de los valores reducidos
sum = 0
for value in valoresr:
    sum += value
media = sum / len(valoresr)
print(f"Media : {media}")

# Calcular la desviación estándar de los valoresr
sum_squares = 0
for value in valoresr:
    sum_squares += (value - media) ** 2
variance = sum_squares / len(valoresr)
desviacion = variance ** 0.5
print(f"Desviación: {desviacion}")

# Coeficiente de variación
coeficiente = (desviacion / media) * 100
print(f"Coeficiente: {coeficiente}")

# RUIDO GAUSSIANO
escala_ruido = 0.7
ruido_gaussiano = []
for _ in range(len(valoresr)):
    ruido_gaussiano.append(escala_ruido * (2 * random.random() - 1))

# RUIDO IMPULSO
desviacion_estandar_ruido_impulso = 0.1
ruido_impulso = []
for _ in range(len(valoresr)):
    ruido_impulso.append(random.gauss(0, desviacion_estandar_ruido_impulso))
    if ruido_impulso[-1] < 0.05:
        ruido_impulso[-1] = 0

# Señal contaminada con ruido gaussiano y ruido impulsivo
signalruido = []
for i in range(len(valoresr)):
    signalruido.append(valoresr[i] + ruido_gaussiano[i] + ruido_impulso[i])

# Generar ruido artefacto
ruido_artefacto = []
for _ in range(len(valoresr)):
    ruido_artefacto.append(random.gauss(0, 0.5))

# Contaminar la señal con ruido artefacto
signal_ruido_artefacto = []
for i in range(len(valoresr)):
    signal_ruido_artefacto.append(valoresr[i] + ruido_artefacto[i])

# Potencia de la señal original
P_signal = 0
for value in valoresr:
    P_signal += value ** 2
P_signal /= len(valoresr)

# Potencia del ruido artefacto
P_noise_artefacto = 0
for value in ruido_artefacto:
    P_noise_artefacto += value ** 2
P_noise_artefacto /= len(ruido_artefacto)

# Calcular SNR de la señal con ruido artefacto
SNR_artefacto = 10 * math.log10(P_signal / P_noise_artefacto)
print("SNR del ruido artefacto:", SNR_artefacto, "dB")

# Potencia de la señal original
P_signal = 0
for value in valoresr:
    P_signal += value ** 2
P_signal /= len(valoresr)

# Potencia del ruido impulsivo
P_noise = 0
for value in ruido_impulso:
    P_noise += value ** 2
P_noise /= len(ruido_impulso)

# Calcular SNR IMPULSO
SNR_impulso = 10 * math.log10(P_signal / P_noise)
print("SNR señal impulso:", SNR_impulso, "dB")

# Potencia de la señal y del ruido
potencia_senial = 0
for value in valoresr:
    potencia_senial += value ** 2
potencia_senial /= len(valoresr)

potencia_ruido = 0
for i in range(len(valoresr)):
    potencia_ruido += (ruido_gaussiano[i] + ruido_impulso[i]) ** 2
potencia_ruido /= len(valoresr)

#  SNR 
SNR_dB = 10 * math.log10(potencia_senial / potencia_ruido)
print(f"SNR : {SNR_dB:.2f} dB")

# Graficar la señal original
plt.figure()
plt.plot(valoresr)
plt.title('Señal Original')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()

# Graficar la señal original (histograma)
plt.figure()
plt.hist(valoresr)
plt.title('Histograma de la Señal Original')
plt.xlabel('Amplitud')
plt.ylabel('Frecuencia')

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

