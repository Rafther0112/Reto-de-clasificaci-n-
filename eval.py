#%%
from model import Model, Descriptor, CatColorHistogram
import os, cv2, sklearn.metrics
import sklearn
import argparse
#%%
if __name__ == '__main__': #Definicion de los parametros para que funcione la evaluacion de una sola imagen por consola
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image', type=str, default="todo", help='Nombre de la imagen que se va a evaluar')
    # args va a almacenar los argumentos que le pasen al script
    args = parser.parse_args()

if args.image == "todo": #Condicional sobre el valor que recibe de la imagen. En caso de que no ingrese ningun nombre y no se use el comando --image, entonces el codigo imprime todos los resultados encontrados
    #load data
    print("\n")
    print("Usted ha seleccionado la opción para visualizar las métricas del modelo de clasificación sobre todas las imágenes de testeo")
    print("Por favor espere mientras se carga el modelo y los descriptores de las imágenes de testeo")
    path_testeo = os.path.join("Rice_Image_Dataset", "Test")
    #imagenes_testeo, anotaciones_testeo = cargar_datos_testeo(path_testeo)
    descriptor_testeo, anotaciones_testeo = Descriptor()
    #load model
    model=Model()
    prediccion = model.predict(descriptor_testeo)
    resultados = sklearn.metrics.precision_recall_fscore_support(anotaciones_testeo, prediccion, average = "weighted", zero_division= 0)
    print("\n")
    print("Ya se ha realizado todo el proceso :)")
    print("\n")
    decision = int(input("Oprima 1 si desea visualizar las métricas obtenidas sobre el conjunto de testeo. Oprima 0 si desea cancelar el proceso: "))
    if decision == 1:
        print("\n")
        print(f"La precisión del modelo desarrollado es: {resultados[0]}")
        print(f"La cobertura del modelo desarrollado es: {resultados[1]}")
        print(f"La F1 medida del modelo desarrollado es: {((2*resultados[0]*resultados[1])/(resultados[0]+resultados[1]))}")
        print("\n")
        print("El proceso ha finalizado exitosamente.")
        print("\n")
    else: 
        print("El proceso ha finalizado existosamente.")
        print("\n")
        None

else: #En este caso solo se presentan los resultados pertenecientes a una imágen.
    print("\n")
    print("Usted ha seleccionado la opción para predecir la categoria de una imagen de interés")
    
    nombre_imagen_evaluacion = args.image
    ruta = os.path.join("Rice_Image_Dataset", "Test", nombre_imagen_evaluacion)
    imagen_evaluacion = cv2.imread(ruta)
    print("Por favor espere un momento mientras se realiza la descripción cuantitativa de su imágen...")
    descriptor_testeo = CatColorHistogram(imagen_evaluacion, 20)
    #load model
    print("Por favor espere un momento mientras se carga el modelo de clasificación... ")
    model=Model()
    prediccion = model.predict([descriptor_testeo])
    anotacion = None
    if nombre_imagen_evaluacion[0] == "A":
        anotacion = "Arborio"

    if nombre_imagen_evaluacion[0] == "b":
        anotacion = "Basmati"

    if nombre_imagen_evaluacion[0] == "I":
        anotacion = "Ipsala"

    if nombre_imagen_evaluacion[0] == "J":
        anotacion = "Jasmine"

    if nombre_imagen_evaluacion[0] == "K":
        anotacion = "Karacadag"
    print("Gracias por su paciencia. Todo se encuentra en orden para brindarle su predicción.")
    print("\n")
    decision = int(input("Oprima 1 si desea visualizar su predicción. Oprima 0 si desea cancelar su proceso: "))
    print('\n')
    if decision == 1:
        print(f"La anotación de esta imágen es: {anotacion}")
        print("\n")
        print(f"La clase predicha para esta imágen es: {prediccion[0]}")
        print("\n")
        print("El proceso ha finalizado exitosamente.")
        print("\n")
    else:
        print("El proceso ha finalizado exitosamente.")
        print("\n")