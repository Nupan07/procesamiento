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
Sección 1: Carga de la Señal

# Formulas desde cero procesamiento largo 

Se carga una señal biomédica desde un archivo llamado charis9 utilizando la biblioteca wfdb.
Se selecciona el tercer canal de la señal y se reduce a 1950 muestras.
Sección 2: Cálculo de la Media y Desviación Estándar

Se calcula la media de la señal reducida utilizando la fórmula: media = (sum(x) / n), donde x es la señal reducida y n es el número de muestras.
Se calcula la desviación estándar de la señal reducida utilizando la fórmula: desviacion = sqrt((sum((x - media) ** 2) / n)), donde x es la señal reducida, media es la media calculada anteriormente y n es el número de muestras.
Sección 3: Coeficiente de Variación

Se calcula el coeficiente de variación utilizando la fórmula: coeficiente = (desviacion / media) * 100, donde desviacion es la desviación estándar calculada anteriormente y media es la media calculada anteriormente.
Sección 4: Generación de Ruido

Se generan tres tipos de ruido:
# Ruido gaussiano:
se utiliza la fórmula ruido_gaussiano = escala_ruido * (2 * random.random() - 1), donde escala_ruido es un parámetro que controla la intensidad del ruido.
# Ruido impulso:
se utiliza la fórmula ruido_impulso = random.gauss(0, desviacion_estandar_ruido_impulso), donde desviacion_estandar_ruido_impulso es un parámetro que controla la intensidad del ruido.
# Ruido artefacto: 
se utiliza la fórmula ruido_artefacto = random.gauss(0, 0.5), donde 0.5 es un parámetro que controla la intensidad del ruido.
# Sección 5:
Contaminación de la Señal

Se contamina la señal original con los tres tipos de ruido generados anteriormente.
# Sección 6:
Cálculo de la Potencia de la Señal y del Ruido

Se calcula la potencia de la señal original utilizando la fórmula: P_signal = (sum(x ** 2) / n), donde x es la señal original y n es el número de muestras.
Se calcula la potencia del ruido artefacto utilizando la fórmula: P_noise_artefacto = (sum(ruido_artefacto ** 2) / n), donde ruido_artefacto es el ruido artefacto generado anteriormente y n es el número de muestras.
# Sección 7:
Cálculo del SNR

Se calcula el SNR (relación señal-ruido) utilizando la fórmula: SNR = 10 * log10(P_signal / P_noise), donde P_signal es la potencia de la señal original y P_noise es la potencia del ruido.
Sección 8: Graficación de los Resultados

Se grafican los resultados utilizando matplotlib, incluyendo la señal original, la señal contaminada con ruido, el ruido gaussiano, el ruido impulsivo y la señal contaminada con ruido artefacto.
Fórmulas Utilizadas

Media: media = (sum(x) / n)
Desviación estándar: desviacion = sqrt((sum((x - media) ** 2) / n))
Coeficiente de variación: coeficiente = (desviacion / media) * 100
Potencia de la señal: P_signal = (sum(x ** 2) / n)
Potencia del ruido:P_noise = (sum(ruido ** 2) / n)
SNR: SNR = 10 * log10(P_signal / P_noise)

