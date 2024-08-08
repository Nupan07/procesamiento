# procesamiento
!pip install wfdb matplotlib numpy
Luego, para importar las librerías necesarias, debes escribir:
import wfdb
import matplotlib.pyplot as plt
import numpy as np
Para descargar las señales, debes escribir:
signal = wfdb.rdrecord("nombre de la señal a utilizar")
# Calcular estadísticas
media = np.mean(signal)
desviacion_estandar = np.std(signal)
coeficiente_variacion = (desviacion_estandar / media) * 100

# Contaminar señal con ruido
escala_ruido = 0.1
ruido_gaussiano = escala_ruido * np.random.randn(len(signal))
ruido_impulsivo = np.random.normal(0, desviacion_estandar_ruido_impulso, len(signal))
ruido_artefacto = np.random.normal(0, 0.5, len(signal))

# Calcular relación señal-ruido (SNR)
P_signal = np.mean(signal ** 2)
P_noise_artefacto = np.mean(ruido_artefacto ** 2)
P_noise = np.mean(ruido_impulsivo ** 2)
SNR_artefacto = 10 * np.log10(P_signal / P_noise_artefacto)
SNR_impulsivo = 10 * np.log10(P_signal / P_noise)
SNR_gaussiano = 10 * np.log10(P_signal / np.mean(ruido_gaussiano ** 2))

# Visualizar resultados
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


