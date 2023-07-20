from model import Model, Descriptor, CatColorHistogram
import os, cv2, sklearn.metrics
import sklearn
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--image', type=str, default="todo", help='Nombre de la imagen que se va a evaluar')
    
    print("Por favor espere mientras se carga el modelo y los descriptores de las imágenes de testeo")
    path_testeo = os.path.join("Rice_Image_Dataset", "Test")
    descriptor_testeo, anotaciones_testeo = Descriptor()

    model=Model()
    prediccion = model.predict(descriptor_testeo)
    resultados = sklearn.metrics.precision_recall_fscore_support(anotaciones_testeo, prediccion, average = "weighted", zero_division= 0)
    accuracy = resultados[0]
    print("You got {}% accuracy".format(round(accuracy*100,2)))

