# Reto de clasificación
Repositorio para el algoritmo de Machine Learning para clasificación de 5 tipos diferentes de arroz.

Para el correcto funcionamiento de la solución planteada se desarrollaron funciones adicionales las cuales se encuentran en el archivo Model.py, donde cada una de estas cumple un rol especifico. Adicionalmente, se adjuntaron 2 archivos .json adicionales, los cuales contienen 1) el modelo de Supporting Vector Machine entrenado y 2) los descriptores finales de las imágenes de testeo. Esto con el objetivo de reducir el coste y tiempo computacional a la hora de probar el algoritmo. 

Para el funcionamiento del modelo es necesario contar con las siguientes librerías, las cuales, en caso de no tener se recomienda instalarlas mediante la terminal haciendo uso del comando pip Install —[README.txt](https://github.com/Rafther0112/Reto-de-clasificaci-n-/files/8887933/README.txt)

	•	CV2		pip install opencv-python
	•	Skelarn		pip install -U scikit-learn
	•	Os		pip install os.path2
	•	Argparse	pip install argparse
	•	Pickle		pip install pickle5
	•	Numpy		pip install numpy
	•	Skimage		pip install scikit-image

Por otro lado, para correr el código presente en el archivo eval.py se recomienda hacer uso de la terminal. Este código cumple con dos funciones, uno para la visualización de las métricas de clasificación obtenidas sobre el conjunto de testeo y otra para realizar la predicción de una imagen de interés. Para el funcionamiento de cada una se hacen las siguientes sugerencias: 
	•	Métricas generales:  Hacer uso del comando python eval.py y seguir las indicaciones que van apareciendo cuando se hace la ejecución. 
	•	Evaluación individual:  Hacer uso del comando python eval.py --image “nombre”
						      En este caso, el nombre que se ingresa es el de la imagen de interés sobre el conjunto de testeo del modelo. Este nombre debe ser fiel a cómo se encuentra guardado e ir entre comillas, por ejemplo, “Karacadag (10864).jpg”.

Finalmente, es fundamental que la base de datos se encuentre a la misma altura del archivo eval.py y de Model.py para que funcione adecuadamente la importación de las imagenes. 



