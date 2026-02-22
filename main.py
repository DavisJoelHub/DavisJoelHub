{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "08db4617",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Iniciando carga de datos...\n",
      "✅ Paso 1 completado con éxito.\n",
      "Total de registros cargados: 165474\n",
      "\n",
      "Primeras 5 filas del dataset:\n",
      "   year  month  day  order  country  session ID  page 1 (main category)  \\\n",
      "0  2008      4    1      1       29           1                       1   \n",
      "1  2008      4    1      2       29           1                       1   \n",
      "2  2008      4    1      3       29           1                       2   \n",
      "3  2008      4    1      4       29           1                       2   \n",
      "4  2008      4    1      5       29           1                       2   \n",
      "\n",
      "  page 2 (clothing model)  colour  location  model photography  price  \\\n",
      "0                     A13       1         5                  1     28   \n",
      "1                     A16       1         6                  1     33   \n",
      "2                      B4      10         2                  1     52   \n",
      "3                     B17       6         6                  2     38   \n",
      "4                      B8       4         3                  2     52   \n",
      "\n",
      "   price 2  page  \n",
      "0        2     1  \n",
      "1        2     1  \n",
      "2        1     1  \n",
      "3        2     1  \n",
      "4        1     1  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def cargar_datos(ruta):\n",
    "    \"\"\"\n",
    "    Función 0: Implementa cargar_datos(ruta) que usa pandas.read_csv \n",
    "    para preparar el DataFrame inicial.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # El dataset de e-shop 2008 usa ';' como separador de columnas\n",
    "        df = pd.read_csv(ruta, sep=';')\n",
    "        return df\n",
    "    except FileNotFoundError:\n",
    "        print(f\"❌ Error: No se encontró el archivo en la ruta: {ruta}\")\n",
    "        return None\n",
    "    except Exception as e:\n",
    "        print(f\"❌ Error inesperado al cargar los datos: {e}\")\n",
    "        return None\n",
    "\n",
    "# --- Bloque de ejecución principal ---\n",
    "if __name__ == \"__main__\":\n",
    "    # Nombre exacto de tu archivo\n",
    "    ruta_dataset = \"e-shop clothing 2008.csv\"\n",
    "    \n",
    "    print(\"Iniciando carga de datos...\")\n",
    "    df = cargar_datos(ruta_dataset)\n",
    "    \n",
    "    if df is not None:\n",
    "        print(\"✅ Paso 1 completado con éxito.\")\n",
    "        print(f\"Total de registros cargados: {len(df)}\")\n",
    "        print(\"\\nPrimeras 5 filas del dataset:\")\n",
    "        print(df.head())\n",
    "    else:\n",
    "        print(\"⚠️ No se pudieron cargar los datos. Revisa que el archivo CSV esté en la misma carpeta.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python Data",
   "language": "python",
   "name": "data"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
