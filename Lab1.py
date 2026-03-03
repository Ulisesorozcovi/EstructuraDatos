## Estructura de datos
## Ulises Orozco
import numpy as np
import os

# Creacion de la matriz
filename = "matriz_objetivo.dat"
### Tamaño solicitado
shape = (100000, 100000)
## Tipo de dato a trabajar
dtype = 'uint8'

def crear_y_poblar_matriz():
    # 1. Crear el archivo de mapeo en disco (Modo 'w+' crea o sobrescribe)
    # Aqui pasamos a trabjar el espacio en disco.
    fp = np.memmap(filename, dtype=dtype, mode='w+', shape=shape)
    
    # 2. PPoblado por bloques
    # Se procesan de 10,000 filas para mantener el uso de RAM bajo
    chunk_size = 10000
    print("Poblando matriz...")
    
    for i in range(0, shape[0], chunk_size):
        end = min(i + chunk_size, shape[0])
        # Generar datos aleatorios (0 y 1) para el bloque
        fp[i:end, :] = np.random.randint(0, 2, size=(end-i, shape[1]), dtype=dtype)
        # Forzar escritura a disco
        fp.flush()
        print(f"Progreso: {end}/{shape[0]} filas escritas.")

    # Mensaje de creacion
    print(f"Archivo creado exitosamente: {filename} ({os.path.getsize(filename) / 1e9:.2f} GB)")
    return fp

# Ejecución y creacion del archivo
# El archivo generado, tiene un peso de 10 GB
m = crear_y_poblar_matriz()