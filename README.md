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

En el análisis de señales biomédicas, es fundamental comprender ciertos estadísticos descriptivos que permiten resumir y caracterizar el comportamiento de la señal. Estos estadísticos ayudan a identificar patrones, tendencias y variaciones que podrían no ser evidentes a simple vista. A continuación, se explican los principales estadísticos utilizados en esta práctica:

## MEDIA :  
La media es una medida de tendencia central que representa el valor promedio de una señal. Se calcula sumando todos los valores de la señal y dividiendo entre el número total de muestras. La media también se conoce como media aritmética o promedio. Además, la media de una distribución estadística es equivalente a su esperanza matemática.

  ![](https://github.com/Nupan07/procesamiento/blob/main/MEDIA.png)

  Donde:

**𝑁: N es el número total de muestras.**
**X: representa cada uno de los valores de la señal.**

## DESVIACIÓN ESTANDAR 

Es una medida de dispersión estadística que indica cuánto se alejan los valores de un conjunto de datos respecto a su media. En otras palabras, refleja el grado de variabilidad o dispersión de los datos: 

  ![](https://github.com/Nupan07/procesamiento/blob/main/Desviaci%C3%B3n.png)

Cuanto mayor sea la desviación estándar de un conjunto de datos, significa que más lejos están los datos de la media. Y la interpretación también se puede hacer al revés, si la desviación estándar es baja quiere decir que en general los datos están muy cerca de su media.

La **desviación estándar** (σ) se calcula con la siguiente fórmula:

Donde:

- \( σ ) es la desviación estándar.
- \( N \) es el número total de observaciones.
- \( x_i \) representa cada valor del conjunto de datos.
- \( \mu \) es la media de los datos.

## COEFICIENTE DE VARIACIÓN 

El coeficiente de variación es una medida estadística que sirve para determinar la dispersión de un conjunto de datos respecto a su media. El coeficiente de variación se calcula dividiendo la desviación típica de los datos entre su promedio.

El coeficiente de variación se expresa en forma de porcentaje y suelen utilizarse las siglas CV como símbolo de esta métrica estadística.

![](https://github.com/Nupan07/procesamiento/blob/main/Coeficiente.png)

El **coeficiente de variación** (CV) se calcula con la siguiente fórmula:

Donde:

- \( \sigma \): desviación estándar.
- \( \mu \): media de los datos.

## INICIO LABORATORIO 

1. Buscaremos en Pysionet y selecionaremos el boton DATA
![](https://github.com/Nupan07/procesamiento/blob/main/Physionet.png)
2. Ingresaremos la sigla EMG (Electromiografia) donde escogeremos la señal de nuestra preferencia donde evidenciaremos toda la informacion referente a esta base de datos.
   En nuestro caso escogimos escoger Stress Recognition in Automobile Drivers
![](https://github.com/Nupan07/procesamiento/blob/main/Physionet2.png)

## Objetivo del estudio 

El objetivo principal del estudio fue investigar la viabilidad del reconocimiento automático del estrés en conductores durante tareas de conducción en el mundo real. Identificar niveles de estrés a partir de señales fisiológicas permite mejorar la seguridad vial y el diseño de sistemas de asistencia al conductor, contribuyendo a la reducción de accidentes relacionados con el estrés.

## Metodologia de adquisición de datos 
Se recopilaron grabaciones multiparamétricas de voluntarios sanos mientras conducían por una ruta prescrita en Boston, Massachusetts. La ruta incluyó tanto calles urbanas como autopistas para simular diferentes niveles de estrés en condiciones de tráfico real.

**🔬 Señales registradas:**

- ECG (Electrocardiograma): para monitorear la actividad eléctrica del corazón.
- EMG (Electromiografía) del trapecio derecho: para evaluar la tensión muscular, un indicador clave del estrés físico.
- GSR (Resistencia Galvánica de la Piel): medida en la mano y el pie, para detectar respuestas del sistema nervioso autónomo.
- Frecuencia respiratoria: para analizar patrones de respiración relacionados con el estrés.

3. Al obtener la base de datos deseada descargaremos nuestros archivos el la parte inferior de FILES en este caso utilizaremos el archivo drive01.dat y .hea donde es **necesario** obtener estos 2 archivos  el **.dat** y **.hea**.
   
   Al descargar estos dos archivos recordemos que se deben encontrar en la misma carpeta


