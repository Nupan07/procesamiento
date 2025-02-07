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

En el análisis de señales biomédicas, es fundamental comprender ciertos estadísticos descriptivos que permiten resumir y caracterizar el comportamiento de la señal. Estos estadísticos ayudan a identificar patrones, tendencias y variaciones que podrían no ser evidentes a simple vista. 

A continuación, se explican los principales estadísticos utilizados en esta práctica:

## MEDIA :  
La media es una medida de tendencia central que representa el valor promedio de una señal. Se calcula sumando todos los valores de la señal y dividiendo entre el número total de muestras. La media también se conoce como media aritmética o promedio. Además, la media de una distribución estadística es equivalente a su esperanza matemática.

  ![](https://github.com/Nupan07/procesamiento/blob/main/MEDIA.png)

  Donde:

**𝑁: N es el número total de muestras.**

**X_i: representa cada uno de los valores de la señal.**

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
   
## Metodologia de graficacion de señal 

# 📊 Cómo Graficar una Señal de EMG

Para poder graficar la señal, lo primero que necesitamos es descargar la librería **`wfdb`**. Esta librería es súper útil porque nos permite leer archivos de datos fisiológicos, como el que vamos a usar. Básicamente, se encarga de abrir el documento descargado y mostrarnos la información que contiene.  

Una vez tengas instalada la librería, el siguiente paso es **cargar el archivo en el compilador** que estés usando. En este caso, trabajaremos con un archivo llamado **`drive01`**. Este archivo contiene varios canales de datos, pero no todos nos interesan, así que lo que haremos será identificar cuál canal necesitamos para nuestra tarea.  

### 🔍 ¿Cómo saber qué canales trae el archivo?  
Aquí hay dos formas de hacerlo:  
1. Puedes escribir una simple línea de código que te muestre los canales guardados.  
2. O si quieres hacerlo más rápido, incluso puedes usar una IA que lea el archivo y te diga cuántos canales hay y cómo se llaman.  

Si prefieres la opción del código, solo necesitas esto:  

canales = record.sig_name 

donde nos saldran los correspondientes canales que se encuentran en nuestra señal el siguiente paso a dar ante esto es seleccionar el canal que utilizaremos en esta caso sera la señal **EMG** , dado que este archivo se organiza de forma matricial , necesitaremos decirle al programa que fila ( canal) queremos leer. Luego le diremos que tome todos los datos  de esa fila para graficarlos.

**Donde utilizaremos la siguiente linea de codgigo :**

voltaje_canal_1 = signal.p_signal[:, 1]  # Selección del canal EMG (posición 1)

- signal.p_signal[:, 1]: Seleccionamos todos los datos (todas las filas) del canal que está en la posición 1.
- voltaje_canal_1: Guardamos estos datos en una variable que llamamos así para mayor claridad, pero puedes nombrarla como prefieras.

## Donde nos arroja la siguiente grafica:

![](https://github.com/Nupan07/procesamiento/blob/main/Se%C3%B1alorginal.png)

A partir de esta grafica iniciaremos con los calculos estadisticos explicados anteriormente, que incluyen:

**RECORDEMOS QUE CADA CALCULO UTILIZAREMOS DOS METODOS UNA PROGRAMADA Y OTRA A MANO**

- **MEDIA:** Nos permite conocer el valor promedio del voltaje en la señal
  
  ## MEDIA PROGRAMADA:
  
En la parte programada utilizaremos la libreria **Numpy** donde su linea de codigo es : **media = np.mean(voltaje)**

## MEDIA A MANO :

La programacion a mano se utiliza un bucle  for que suma todas las columnas de la fila y las divide por la cantidad de datos que se encuentran en la misma columna, donde se utilizo un contador que este igualado a 0 para que se repita el proceso 

En la parte a mano utilizaremos unicamente **FOR** y el contador igualado a 0 donde su linea de codigo es : 

 **datos=data.copy()
 
    datos.tolist()
    
    total=0.0
    
    contador=0
    
    for x in data:
    
      total+=x
      
      contador+=1
      
    return total/contador if contador != 0 else 0.0**
    
   1.**contador+=1** 
    Simplemente se incrementa el contador en uno por cada iteración, lo que nos permite contar cuántos elementos hay en data.
Después del bucle, habra una instrucción return que calcula y devuelve un valor.


 - **DESVIACIÓN ESTANDAR** Nos dará una medida de la dispersión de los datos, indicando qué tan alejados están los valores individuales respecto a la media.

  ## DESVIACIÓN ESTANDAR PROGRAMADA:

  En la desviación estandar seguiremos utilizando la libreria **Numpy** donde su linea de codigo sera : **desviacion = np.std(voltaje)**

  ## DESVIACIÓN ESTANDAR A MANO:

  **for x in data:
      diferencia_raiz_suma += (x - mean) ** 2
      contador+=1
    return (diferencia_raiz_suma / contador) ** 0.5 if contador != 0 else 0.0**

Ante esta linea de codigo primero, tenemos un bucle for que recorre  sobre cada elemento x en una lista llamada data. es una lista que contiene los datos , ya sea enteros o flotantes.

**Dentro del bucle for tenemos  dos operaciones**}

1. diferencia_raiz_suma += (x - mean) ** 2 . La cual donde cada x , sera restada por el valor ya obtenido de mean ( media) y sera elevado al cuadrado , cada valor suma el cuadrado el valor dado para luego ser sumado a **diferencia_raiz_suma** que esta evaluado a un valor 0.0
2. **contador += 1**
   
Simplemente se  incrementa el contador en uno por cada iteración, lo que nos permite contar cuántos elementos hay en data.
Después del bucle, habra una instrucción return que calcula y devuelve un valor.

**(diferencia_raiz_suma / contador) ** 0.5**
Donde primero, se  divide diferencia_raiz_suma por contador, lo que es equivalente a calcular el promedio de los cuadrados de las diferencias respecto a la media.
Luego, se eleva este promedio a la potencia de 0.5, que es lo mismo que tomar la raíz cuadrada.
if contador != 0 else 0.0
Esto es una expresión condicional que dice: si contador no es cero, entonces realiza el cálculo mencionado; de lo contrario, devuelve 0.0

- ## COEFICIENTE DE VARIACIÓN

  Este estara expresado en porcentaje, el cual nos ayudará a comparar la variabilidad relativa de la señal, independientemente de su magnitud.

## COEFICIENTE DE VARIACION PROGRAMADA 

 Donde su linea de codigo sera :  **coef_var = desviacion / media**

## COEFICIENTE DE VARIACIÓN A MANO 

La linea de codigo utilizada para esta parte es 

datos=data.copy()

    datos.tolist()
    
    mean = custom_mean(data)
    
    if mean == 0:
    
        return 0.0  
        
    return (custom_std_dev(data) / mean) * 100

Dando por finalizada los calculos estadisticos en este laboratorio , siendo a continuacion se hara la explicacion del Histograma con su respectiva campana de Gauss , ante esto primero comprenderemos brevemente que es la campana de Gauss

## CAMPANA DE GAUSS 

La campana de Gauss, es conocida como la distribución normal, donde su tipo de distribución de probabilidad  se representa gráficamente como una curva en forma de campana.

  ## HISTOGRAMA 

Ante los calculos estadisticos anteriores se grafica un histograma de la media el cual se aplicara la campana de Gauss para demostrar la distribucion real de los datos , donde para sacar correspondiente grafica se utilizo el siguiente fragmento de codigo 

 # Crear histograma
 
    plt.figure(figsize=(10, 6))
    
    plt.hist(voltaje, bins=50, color='skyblue', edgecolor='black', density=True, label='Histograma')

  ## Crear la curva de Gauss
  
    x = np.linspace(min(voltaje), max(voltaje), 1000)
    
    gauss = norm.pdf(x, loc=media, scale=desviacion)
    
    plt.plot(x, gauss, color='red', linewidth=2, label='Campana de Gauss')

En esta parte del codigo lo que se logra hacer graficar los datos para que nos de el histograma logrando variar el ancho y el largo de la grafica de la media y en la creacion de la curva de Gauss se logra modificar el color y el grosor de la linea.

Como se observa la grafica y la campana dan los valores reales mostrando que la mayoria de valores se encuentran en el centro generando asi la campana , dando a continuacion la muestra del resultado 

![](https://github.com/Nupan07/procesamiento/blob/main/Histograma.png)

## APLICACION DE RUIDO GAUSSIANO , RUIDO IMPULSO Y RUIDO ARTEFACTO

 A continuacion a nuestra señal orginal se  le aplico 3 diferentes ruidos los cuales son :
 
  **RUIDO GAUSSIANO:**
  El ruido gaussiano es un tipo de ruido aleatorio que sigue una distribución normal, también conocida como distribución gaussiana. Esto significa que los valores del ruido se distribuyen alrededor de una media (generalmente cero) con una desviación estándar específica. La distribución es simétrica y la mayoría de los valores están cerca de la media, disminuyendo gradualmente a medida que nos alejamos de ella.

Donde la linea de codigo para aplicar este ruido a nuestra señal fue :

**ruido_gaussiano = np.random.normal(0, desviacion, voltaje_canal_1.shape)**

  **voltaje_contaminado = voltaje_canal_1 + ruido_gaussiano**
            
   **SNR_gaussiano = calcular_SNR(voltaje_canal_1, ruido_gaussiano)**
   
Esta línea de código genero  un ruido gaussiano con una media de 0 y una desviación estándar definida por la variable desviacion, y la  suma al voltaje original de voltaje_canal_1 para obtener una señal contaminada llamada voltaje_contaminado. Luego, la se llama a la función calcular_SNR la cual calcula la relación señal/ruido (SNR) entre el voltaje original y el ruido añadido.





 ## Analisis de datos estadisticos 
 
La señal de electromiografía (EMG) analizada presenta una media de -0.0055 mV, lo que indica que, en promedio, la actividad muscular registrada se mantiene en un nivel bajo. La mediana de -0.0047 sugiere que la mayor parte de los valores se encuentran cerca de este punto, lo que indica que la señal tiene una distribución ligeramente sesgada, posiblemente debido a picos de actividad o ruido presente en la medición.

La desviación estándar de  0.0411 mV refleja una variabilidad considerable en la señal, lo que sugiere cambios en la actividad muscular a lo largo del tiempo. Finalmente, el coeficiente de variación del 753.52% muestra que la variabilidad relativa de la señal es muy alta en comparación con su media, lo que puede deberse a fluctuaciones bruscas en la actividad muscular o a la presencia de ruido en la adquisición de datos.

Estos resultados indican que la señal presenta una gran dispersión y valores extremos que pueden influir en la interpretación de la actividad muscular, por lo que es recomendable analizar su espectro de frecuencia o aplicar técnicas de filtrado para reducir posibles interferencias.










  





