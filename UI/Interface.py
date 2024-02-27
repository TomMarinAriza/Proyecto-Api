import API.API


print("Bienvenido a su programa para hacer la busqueda de casos positivos a covid\n")
busqueda_departamento = input("Digite el nombre del departamento \n")
control = True

while (control):
    limite_registros = input("Digite el limite de registros a visualizar ")
    if (int(limite_registros) >=100):
        print("Valor no valido\n")
    else:
        control =False


table = API.API.Get_data(int(limite_registros),busqueda_departamento)

columnas_deseadas = ["ciudad_municipio_nom","departamento_nom","edad","tipo_recuperacion","estado"]

table = table[columnas_deseadas]
print(table)

