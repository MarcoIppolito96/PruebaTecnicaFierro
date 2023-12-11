import csv
import os

def lecturaArchivo(archivo_csv):
    if not os.path.exists(archivo_csv):
        print(f"El archivo {archivo_csv} no existe.")
        return
    
    with open(archivo_csv, 'r', newline='', encoding='utf-8') as archivo_csv:

        datos_csv = csv.reader(archivo_csv)

        # Leo la cabecera
        cabecera = next(datos_csv)
        dicc = {}
        for fila in datos_csv:
            #fila = next(datos_csv)
            key = fila[5]
            hora = int(fila[3][-8:-6])

            if 6 <= hora < 12:
                if key in dicc:
                    dicc[key].append(hora)
                else:
                    dicc[key] = [hora]

        dicc_cantidades = {estacion: len(lista) for estacion, lista in dicc.items()}

        #print(dicc)
        print(dicc_cantidades)

        claves_ordenadas = sorted(dicc_cantidades, key=dicc_cantidades.get, reverse=True)

        # Tomar las tres primeras claves
        origenes_mas_calientes = claves_ordenadas[:3]

        return origenes_mas_calientes
    
lecturaArchivo("trips_2023.csv")