import pandas as pd

def cargar_datos(ruta):
    """
    Función 0: Implementa cargar_datos(ruta) que usa pandas.read_csv 
    para preparar el DataFrame inicial.
    """
    try:
        # El dataset de e-shop 2008 usa ';' como separador
        df = pd.read_csv(ruta, sep=';')
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

if __name__ == "__main__":
    # Prueba de la función con tu archivo
    ruta_dataset = "e-shop clothing 2008.csv"
    datos = cargar_datos(ruta_dataset)
    if datos is not None:
        print("✅ Carga exitosa. Primeras filas:")
        print(datos.head())