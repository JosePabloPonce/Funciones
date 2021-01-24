# DescuentosYConversion
# 26/04/19
# Diego Alvarez 19498
# Jose Ponce
# seccion 60
# Se calculan los descuentos y se hace la conversion a dolares


# Era mas efectivo hacer de una vez los calculos que hacer un validacion como se hizo en el diseño
# Se reciben dos variables que contienen en forma de lista
# la cantidad de ingredientes de hamburguesa y sandwiches respectivamente
def Descuentos(Cantidades,Cantidades2):
    if Cantidades[0]>100:
        Dpanes = 0.25*Cantidades[0]
        des1 = 0.10*Dpanes
    elif Cantidades[0]<100:
        Dpanes = 0.25*Cantidades[0]
        des1 = 0
    if Cantidades[1]>30:
        Dcarne = 1.50*Cantidades[1]
        des2 = 0.15*Dcarne
    elif Cantidades[0]<30:
        Dcarne = 1.50*Cantidades[1]
        des2 = 0    
    if Cantidades2[0]>100:
        DpanesS = 0.20*Cantidades2[0]
        des3 = 0.05*DpanesS
    elif Cantidades2[0]<100:
        DpanesS = 0.20*Cantidades2[0]
        des3 = 0   
    if Cantidades2[1]>50:
        Dpechugas = 1.00*Cantidades2[1]
        des4 = 0.05*Dpechugas
    elif Cantidades2[1]<50:
        Dpechugas = 1.00*Cantidades2[1]
        des4 = 0
    return [Dpanes, des1, Dcarne, des2, DpanesS, des3, Dpechugas, des4]

# Se reciben todos los valores de los ingredientes y se convierten a quetzales
def ConversionDolares(ValidacionG):
    ValidacionG[0] = ValidacionG[0]*7
    ValidacionG[1] = ValidacionG[1]*7
    ValidacionG[2] = ValidacionG[2]*7
    ValidacionG[3] = ValidacionG[3]*7
    ValidacionG[4] = ValidacionG[4]*7
    ValidacionG[5] = ValidacionG[5]*7
    ValidacionG[6] = ValidacionG[6]*7
    ValidacionG[7] = ValidacionG[7]*7
    return ValidacionG
