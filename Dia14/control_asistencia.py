import os
import numpy
import cv2
import face_recognition as fr
from _datetime import datetime

#crear base de datos
ruta = 'Empleados'
registro_csv = 'registro.csv'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

#codificar imagenes
def codificar(imagenes):
    #crear lista nueva
    lista_codificada = []
    #pasar las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        #CODIFICAR
        codificado = fr.face_encodings(imagen)[0]
        #agregar a la lista
        lista_codificada.append(codificado)
    return lista_codificada

# Verificar y limpiar el registro diario
def verificar_registro_diario():
    if os.path.exists(registro_csv):
        with open(registro_csv, 'r') as f:
            primera_linea = f.readline()
            if datetime.now().date().isoformat() not in primera_linea:
                open(registro_csv, 'w').close()


#Registrar los ingresos
def registrar_ingresos(persona):
    f = open(registro_csv, 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])
    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')

def main():
    lista_empleados_codificada = codificar(mis_imagenes)

    #tomar una imagen de camara web
    captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        #leer imagen de la camara
        exito, imagen = captura.read()
        if not exito:
            print('no se ha podido tomar la captura')
        else:
            #reconocer cara en captura
            cara_captura = fr.face_locations(imagen)
            #codificar cara capturada
            cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
            #buscar coincidencias
            for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
                coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
                distancias = fr.face_distance(lista_empleados_codificada, caracodif)

                print(distancias)

                indice_coincidencia = numpy.argmin(distancias)

                #mostrar coincidencias
                if distancias[indice_coincidencia] >0.6:
                    print("No conicide con ninguno de los empleados")
                else:
                    #buscar nombre del empleado encontrado
                    nombre = nombres_empleados[indice_coincidencia]

                    y1, x2, y2, x1 = caraubic
                    cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 2555, 255), 1)

                    registrar_ingresos(nombre)
                    #mostrar la imagen optenida
                    cv2.imshow('Imagen web', imagen)
                    #mantener ventana abierta
                    cv2.waitKey(0)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                captura.release()
                cv2.destroyAllWindows()
        break


if __name__ == '__main__':
    main()
