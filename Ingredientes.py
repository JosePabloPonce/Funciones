# Ingredientes
# 26/04/19
# Diego Alvarez 19498
# Jose Ponce
# seccion 60
# Se calculan la cantidad de ingredientes


# se reciben las cantidades de hamburguesas y de sandwiches y se convierten a float, se regresan como lista
def esConvertible(Chamburguesas,Csandwiches):
    Chamburguesas = float(Chamburguesas)
    Csandwiches = float(Csandwiches)
    return [Chamburguesas,Csandwiches]
# se reciben las cantidades de hamburguesas y se calcula la cantidad de carne y panes, se regresan como lista
def IngredientesHamburguesa(Convertible):
    Cpanes = Convertible[0]*2
    Ccarne = Convertible[0]*2
    return [Cpanes,Ccarne]
# se reciben las cantidades de sandwiches y se calcula la cantidad de pollo y panes, se regresan como lista
def IngredientesSandwiches(Convertible):
    CpanesS = Convertible[1]*3
    Cpollo = Convertible[1]*1
    return [CpanesS,Cpollo]



        
    

    
    
    
    
    
    
    
    