import UI.Interface
import API.API
import Imputing.method
import pandas as pd

# Establecer la opción para que pandas no trunque la visualización
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def print_table(limite_registros, busqueda_departamento):
    table = API.API.Get_data(int(limite_registros), busqueda_departamento)
    columnas_deseadas = ["ciudad_municipio_nom", "departamento_nom", "edad", "tipo_recuperacion", "estado"]
    table = table[columnas_deseadas]
    print("Tabla con datos faltantes o corruptos \n",table, "\n")
    final_table = Imputing.method.imputar_datos(table)
    print("Tabla con datos imputados \n",final_table)

def repeticion_tabla():
    controlador = True
    while controlador:
        print("Bienvenido a su programa para hacer la búsqueda de casos positivos a covid\n")
        print_table(UI.Interface.control_register(), UI.Interface.control_department(UI.Interface.departamentos))
        answer = input("Desea realizar otra consulta S/N: ")
        if answer.upper() == "N":
            controlador = False
            print("Gracias por usar el programa")

repeticion_tabla()
