

departamentos = {"AMAZONAS","ANTIOQUIA","ARAUCA","ATLANTICO",
                 "BOLIVAR" , "BOYACA" , "CALDAS" ,"CAQUETA",
                 "CASANARE" ,"CAUCA" ,"CESAR" , "CHOCO",
                 "CORDOBA" , "CUNDINAMARCA" , "GUANIA",
                 "GUAVIARE" , "HUILA", "GUAJIRA" , "MAGDALENA",
                 "META" , "NARIÑO" ,  "SANTANDER", "PUTUMAYO",
                 "QUINDIO" , "RISARALDA" , "NORTE SANTANDER" , "SUCRE",
                 "TOLIMA" , "VALLE" , "VAUPES" , "VICHADA"
                 }




def control_department(lista_departamentos):
    control = True
    while control:
        busqueda_departamento = input("Digite el nombre del departamento \n")
        if busqueda_departamento.upper() not in map(str.upper, lista_departamentos):
            print("Departamento no válido. Inténtelo de nuevo.\n")
        else:
            control = False
    return busqueda_departamento.upper()


def control_register():
    control = True
    while (control):
        limite_registros = input("Digite el limite de registros a visualizar ")
        if (int(limite_registros) >= 100):
            print("Valor no valido\n")
        else:
            control = False
    return limite_registros


