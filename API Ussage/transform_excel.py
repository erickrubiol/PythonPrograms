'''
    Este programa:
        1. Lee los archivos de una ruta si son de Nielsen y los clasifica segun su extension.
        2. Los transforma hasta convertirlos en una única tabla.
        3. Exporta el resultado en un archivo .csv
    
    Se asume que el nombre de los archivo sigue esta estructura:
        Nielsen - Extraccion Papel Higienico Wm_Nacional y areas a P10'20.xlsx
'''

import os
import pandas as pd
import xlrd
from datetime import datetime, date, timedelta
 
# Ruta de lectura
folder = 'c:\\Users\\erick\\Desktop\\Archivos'
ruta_de_salida = 'c:\\Users\\erick\\Desktop\\'
lista_campos = ['Periodo', 'Region', 'Country', 'Item Type']

all_files = []


def inicio_del_mes():
    #Devuelve el primer día del mes actual en formato de fecha
    return datetime.now().date().replace(day=1)

def anio():
    # Año actual en formato YY convertido a texto
    return str((inicio_del_mes() - timedelta(days=1)).year)[-2:]

def mes():
    # Mes anterior al actual en formato MM convertido a texto
    return ("00" + str((inicio_del_mes() - timedelta(days=1)).month))[-2:] 

def mes_ant():
    # Mes anterior a mes() en formato MM, el lag de 32 dias garantiza dos meses de retraso
    return ("00" + str((inicio_del_mes() - timedelta(days=32)).month))[-2:]

def valid_period(file_name):
    # Valida que el periodo del archivo se encuntre entre los dos meses anteriores 
    if file_name.split('.')[0][-5:][-2:] == anio() and file_name.split('.')[0][-5:][:2] in [mes(), mes_ant()]:
        return True
    else:
        return False
        
def valid_extension(file_name):
    # Valida si un archivo tiene la extensión correcta
    if file_name.endswith(".xls") or file_name.endswith(".xlsx"):
        return True
    elif file_name.endswith(".xlsb"):
        return True
    else:
        return False

def valid_file(file_name):
    # Valida que el archivo cumpla las tres condiciones para considerarse valido
    if valid_extension(file_name) and valid_period(file_name) and file_name.startswith("Nielsen"):
        return True
    else:
        return False

def list_of_files(file_path):
    # Crea una lista con los archivos del directorio que son validos en fecha y extensión
    for subfolder, folder, files in os.walk(file_path):
        [all_files.append(subfolder + os.sep + file) for file in files if valid_file(file)]

def export_to_csv(df, filename):
    df.to_csv(ruta_de_salida + filename, index = False)


def main():

    list_of_files(folder)

    # Por cada archivo valido se crea un DF que se anexa al dataframe vacío
    data = pd.DataFrame(columns=lista_campos + ['Value'])

    for i in all_files:
        if i.endswith(".xlsb"):
            # Leer archivo binario Excel
            df = pd.read_excel(i, engine='pyxlsb')
        elif i.endswith(".xls") or i.endswith(".xlsx"):
            df = pd.read_excel(i)
            # xlwb = xlApp.Workbooks.Open(filename, False, True, None, password)

        # Elimina las primeras filas que no tienen datos
        top_row = df.index[df['Unnamed: 0'] == 'Region'].tolist()
        df = df.iloc[top_row[0]:]
        df = df.reset_index(drop=True)

        # Promover primera fila como encabezado de columna
        new_header = df.iloc[0] 
        df = df[1:] 
        df.columns = new_header 

        # Selecciona solo las columnas necesarias
        row_value = i.split('.')[0][-6:-3] + "'" + i.split('.')[0][-2:]
        df['Periodo'] = row_value
        df2 = df[lista_campos + [row_value]]
        df2.rename(columns = {row_value:'Value'}, inplace = True) 


        # Combina los dataframes en uno solo
        data = data.append(df2, ignore_index=True)

    export_to_csv(data, 'nielsen.csv')


if __name__ == "__main__":
    main()