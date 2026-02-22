import pandas as pd

# --- DEFINICIÓN DE FUNCIONES (Primero) ---

def cargar_datos(ruta):
    try:
        df = pd.read_csv(ruta, sep=';')
        return df
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return None

def get_country_name(df):
    mapping = {
        1: "Australia", 2: "Austria", 3: "Belgium", 12: "unidentified",
        29: "Poland", 41: "United Kingdom", 42: "USA", 44: "com"
    }
    df['COUNTRY_NAME'] = df['country'].map(mapping)
    return df

def clean_currency_data(df):
    df = df.dropna(subset=['price'])
    df = df[df['price'] > 0]
    return df

# --- BLOQUE DE EJECUCIÓN (Al final) ---

if __name__ == "__main__":
    ruta_dataset = "e-shop clothing 2008.csv"
    df = cargar_datos(ruta_dataset)
    
    if df is not None:
        # Ahora sí, Python ya conoce estas funciones
        df = get_country_name(df)
        df = clean_currency_data(df)
        
        print("✅ Análisis de Data Architect completado.")
        print(df[['country', 'COUNTRY_NAME', 'price']].head())