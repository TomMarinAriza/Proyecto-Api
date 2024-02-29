import API.API

departamentos = {"AMAZONAS","ANTIOQUIA","ARAUCA","ATLANTICO",
                 "BOLIVAR" , "BOYACA" , "CALDAS" ,"CAQUETA",
                 "CASANARE" ,"CAUCA" ,"CESAR" , "CHOCO",
                 "CORDOBA" , "CUNDINAMARCA" , "GUANIA",
                 "GUAVIARE" , "HUILA", "GUAJIRA" , "MAGDALENA",
                 "META" , "NARIÑO" ,  "SANTANDER", "PUTUMAYO",
                 "QUINDIO" , "RISARALDA" , "NORTE SANTANDER" , "SUCRE",
                 "TOLIMA" , "VALLE" , "VAUPES" , "VICHADA"
                 }


def Menssages ():
    print("Bienvenido a su programa para hacer la busqueda de casos positivos a covid\n")
def Control_deparment(lista_departamentos):
    control = True
    while (control):
        busqueda_departamento = input("Digite el nombre del departamento \n")
        if (busqueda_departamento not in lista_departamentos):
            print("Departamento no valido digitelo otra vez \n")
        else:
            control = False
    return busqueda_departamento

def Control_register():
    control = True
    while (control):
        limite_registros = input("Digite el limite de registros a visualizar ")
        if (int(limite_registros) >= 100):
            print("Valor no valido\n")
        else:
            control = False
    return limite_registros

def Print_Table (limite_registros,busqueda_departamento):

    table = API.API.Get_data(int(limite_registros), busqueda_departamento)

    columnas_deseadas = ["ciudad_municipio_nom", "departamento_nom", "edad", "tipo_recuperacion", "estado"]

    table = table[columnas_deseadas]
    print(table)

def Cicle ():
    controlator = True

    while (controlator):
        Menssages()
        Print_Table(Control_register(),Control_deparment(departamentos))
        answer = input("Desea realizar otra consulta S/N  ")
        if answer == "N":
            controlator = False
            print("Gracias por usar el programa")
