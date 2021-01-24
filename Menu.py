# Restaurante
# 26/04/19
# Diego Alvarez 19498
# Jose Ponce
# seccion 60
# Resultados de pedido de hamburguesas y sandwiches del restaurante


from Ingredientes import *
from DescuentosYConversion import *
from Contabilidad import *

ordenes=0
ingreso=0
menu = True
# Se inicia variable menu para que funcione el ciclo while
while menu == True :
    print("Bienvenido al menu de registro de pedidos")
    print("Elija una opcion")
    print("1. Ingresar un pedido")
    print("2. Salir")
    pedido = input("")
    if pedido == "1":
        Chamburguesas = input("Ingrese cantidad de hamburguesas: ")
        Csandwiches = input("Ingrese cantidad de sandwiches: ")
        print("+++++++++++++Reporte de ingredientes del pedido+++++++++++++")
        
        Conversion = esConvertible(Chamburguesas,Csandwiches)
        Cantidades = IngredientesHamburguesa(Conversion)
        #print(Cantidades)
        
        Conversion2 = esConvertible(Chamburguesas,Csandwiches)
        Cantidades2 = IngredientesSandwiches(Conversion2)
        #print(Cantidades2)
        #Descuentos
        ValidacionG= Descuentos(Cantidades,Cantidades2)
        
        ConversionD = ConversionDolares(ValidacionG)
        
        #Ingresos
        ingresogenerado = Ingresos(Conversion[0], Conversion[1])
        #Costos TOTAL DE TODO
        ingresonetos = IngresoNeto(ConversionD)
        #Ingresos netos (Ganancias)
        ingresonetofinal = IngresoNetoFinal (ingresonetos,ingresogenerado)
        #Promedio de ingresos
        ingreso += ingresonetofinal
        ordenes += 1
        promedio = PromedioIngresoFinal(ingreso, ordenes)
        #Mantenerse el promedio
        mantenerse = NecesarioParaMantenerse(promedio)
        
        
        
        print("----------Hamburguesa----------")
        print("----------Panes----------")
        print("El costo por ", Cantidades[0],"unidades de pan en Quetzales es de: ", ConversionD[0])
        print('El descuento es de', ConversionD[1])
        print('El total es', ConversionD[0]-ConversionD[1])
        print("----------Carne----------")
        print("El costo por ", Cantidades[1],"unidades de carne en Quetzales es de: ", ConversionD[2])
        print('El descuento es de', ConversionD[3])
        print('El total es', ConversionD[2]-ConversionD[3])
        print("----------Sandwiches de pollo----------")
        print("----------Sandwich----------")
        print("El costo por ", Cantidades[0],"unidades de pan sandwich en Quetzales es de: ", ConversionD[4])
        print('El descuento es de', ConversionD[5])
        print('El total es', ConversionD[4]-ConversionD[5])
        print("----------Pechugas----------")
        print("El costo por ", Cantidades[0],"unidades de pollo en Quetzales es de:", ConversionD[6])
        print('El descuento es de', ConversionD[7])
        print('El total es', ConversionD[6]-ConversionD[7])
        print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        print("El Costo total es Q",ingresonetos)
        print("Este pedido ha generado un ingreso total de Q",ingresogenerado)
        print("El ingreso neto obtenido(ganancia) es Q",ingresonetofinal)
        print("El promedio de ingreso neto obtenido es Q",promedio)
        print("Se necesitaria un proximo ingreso neto de Q",mantenerse, "para llevar el promedio a Q250.00")

        
# Si se desea salir, el menu cambia su valor a falso para detener el ciclo
    elif pedido == "2":
        menu = False
        
        