# procesamiento
Requisitos previos
Paquetes de Python: Necesitarás instalar tres paquetes adicionales: wfdb, matplotlib y numpy. Puedes instalarlos utilizando pip, que es el gestor de paquetes de Python.
wfdb: Para trabajar con las señales de Physionet.
matplotlib: Se utiliza para crear gráficos y visualizaciones de datos.
numpy: Para operaciones matemáticas y de cálculo.

Para instalar iniciaremos en la terminal en este caso Spyder ejecuta el siguientes comando pip install wfdb Al ser instalada escribiremos Import wfdb e importaremos matplotlib.pyplot as plt se utiliza para crear gráficos y visualizaciones de datos Descarga las señales : Ve a Physionet y descarga los archivos .dat y .hea de la señal que deseas analizar. llamaremos la señal signal = wfdb.rdrecord("nombre de la señal a utilizar") En el cual iniciaremos a sacar las estadisticas de nuestra señal Media: se calcula utilizando la fórmula np.mean(valoresr) Desviación estándar: se calcula utilizando la fórmula np.std(valoresr) Coeficiente de variación: se calcula utilizando la fórmula (desviacion/media)*100 
3. Contaminación con ruido
Se contaminan la señal con tres tipos de ruido:
Ruido gaussiano: se genera utilizando la fórmula escala_ruido * np.random.randn(len(valoresr)) Ruido impulsivo: se genera utilizando la fórmula np.random.normal(0, desviacion_estandar_ruido_impulso, len(valoresr)) Ruido artefacto: se genera utilizando la fórmula np.random.normal(0, 0.5, len(valoresr)) 
4. Relación señal-ruido (SNR)
Se calcula la relación señal-ruido (SNR) para cada tipo de ruido:
SNR del ruido artefacto: se calcula utilizando la fórmula 10 * np.log10(P_signal / P_noise_artefacto) SNR del ruido impulsivo: se calcula utilizando la fórmula 10 * np.log10(P_signal / P_noise) SNR de la señal con ruido gaussiano y ruido impulsivo: se calcula utilizando la fórmula 10 * np.log10(potencia_senial / potencia_ruido) 
5. Visualización
Se grafican la señal original, la señal contaminada con ruido, el ruido gaussiano, el ruido impulsivo y la señal contaminada con ruido artefacto utilizando la librería matplotlib.

