📝 Descripción
Este laboratorio implementa el análisis estadístico de señales biomédicas, permitiendo comprender mejor sus características, como la amplitud y la frecuencia. Además, se evalúa cómo estas señales reaccionan al ser contaminadas con diferentes tipos de ruido (gaussiano, impulsivo y de artefacto), analizando su impacto en la calidad de la señal mediante la relación señal/ruido (SNR).

A continuacion ingresaremos a la base de datos  Pysionet , donde buscaremos una señal ECG de nuestra preferencia , la cual importaremos y graficaremos en cualquier compilador en este caso usaremos Spyder. Se recomienda utilizar la libreria matplotlib  para graficar en Python.
## Requisitos
Este laboratorio requiere las siguientes bibliotecas:
- `numpy`
- `pandas`
- `matplotlib`
- `wfdb`
- `from scipy.stats import norm`  # Para calcular la curva de Gauss
  Puedes instalar las bibliotecas necesarias ejecutando:

pip install numpy pandas matplotlib wfdb

## Objetivos 
- Identificar y comprender las características fundamentales de señales biomédicas
- Calcular estadísticos descriptivos (media, desviación estándar, coeficiente de variación, histogramas y funciones de probabilidad) para analizar el comportamiento de las señales.
- Implementar algoritmos en Python para el procesamiento y análisis estadístico de señales fisiológicas.
- Evaluar el impacto del ruido (gaussiano, impulsivo y de artefacto) en las señales biomédicas mediante el cálculo de la relación señal/ruido (SNR).


## Estructura
**🔬 Fundamento Teórico**

1. Buscaremos en Pysionet y selecionaremos el boton DATA
![](https://github.com/Nupan07/procesamiento/blob/main/Physionet.png)
2. Ingresaremos la sigla EMG (Electromiografia) donde escogeremos la señal de nuestra preferencia donde evidenciaremos toda la informacion referente a esta base de datos.
   En nuestro caso escogimos escoger Stress Recognition in Automobile Drivers
   



