import os
import re
import time
from datetime import datetime

dir = "Mi_Gran_Directorio"
patron = re.compile(r'N[a-zA-Z]{3}-\d{5}')


def buscar_numeros_serie(dir):
    start_time =time.time()
    resultados = []

    for root, dirs, files in os.walk(dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    match = patron.search(content)
                    if match:
                        resultados.append((file, match.group()))
            except Exception as e:
                print(f"Error leyendo archivo {file}: {e}")
    return resultados, round(time.time() - start_time, 0)


def imprimir_resultados() :
    resultados_str = ""
    for archivo, numero_serie in resultados:
        resultados_str += f"{archivo:20} {numero_serie}\n"

    resultado = f"""
        ------------------------------------
        Fecha de búsqueda: {fecha_hoy}

        ARCHIVO              NRO. SERIE
        -------              ---------
        {resultados_str}
        Números encontrados: {len(resultados)}
        Duración de la búsqueda: {int(duracion)} segundos
        ------------------------------------
        """
    print(resultado)


resultados, duracion = buscar_numeros_serie(dir)
fecha_hoy = datetime.now().strftime('%d/%m/%y')
imprimir_resultados()
