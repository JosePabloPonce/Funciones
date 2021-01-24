# Contabilidad
# 26/04/19
# Diego Alvarez 19498
# Jose Ponce
# seccion 60
# Se calculan los ingresos, ganancias y costos finales


# Se recibe la cantidad de hamburguesas y de sandwiches
# Se calcula cuanto se ingresa por cada una y se suman para conocer el ingreso final
def Ingresos (Chamburguesas,Csandwiches):

    IngresoHamburguesas = Chamburguesas *25
    IngresoSandwich = Csandwiches *20
    IngresoFinal = IngresoSandwich + IngresoHamburguesas
    return IngresoFinal
# Se reciben los costos de cada ingrediente en una lista y se calcula el costo con el descuento efectuado si se diera el caso
# Se calcula el costo total
def IngresoNeto(ConversionD):
    
    Costo1= ConversionD[0]-ConversionD[1]
    Costo2= ConversionD[2]-ConversionD[3]
    Costo3= ConversionD[4]-ConversionD[5]
    Costo4= ConversionD[6]-ConversionD[7]
    CostoFinal=Costo1+Costo2+Costo3+Costo4
    return CostoFinal

# Se calcula las ganancias restando los ingresos con los costos 
def IngresoNetoFinal(CostoFinal,IngresoFinal):
    NetoFinal= IngresoFinal - CostoFinal
    return NetoFinal

    

def PromedioIngresoFinal (Ingreso, Ordenes):
    promedioingreso = Ingreso / Ordenes
    return promedioingreso

def NecesarioParaMantenerse (promedioingreso):
    if promedioingreso < 250:
        mantenerse= (250-promedioingreso)+250
        return mantenerse
    elif promedioingreso > 250:
        mantenerse=250-(promedioingreso-250)
        return mantenerse
    else:
        return 250