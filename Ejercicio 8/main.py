from Clase import Conjunto

def menu():
    print("Seleccione una opción : ")
    print("1.Unión conjuntos")
    print("2 Diferencia conjuntos")
    print("3.Verificar conjuntos son iguales")
    print("4.Salir")
    
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        elementos1 = input("Ingrese los elementos del primer conjunto: ")
        elementos2 = input("Ingrese los elementos del segundo conjunta: ")
        conjunto1 = Conjunto(elementos1.split(","))
        conjunto2 = Conjunto(elementos2.split(","))
        resultado = conjunto1 + conjunto2
        print("La unión de los conjuntos es:", resultado.elementos)
        
    elif opcion == 2:
        elementos1 = input("Ingrese los elementos del primer conjunto: ")
        elementos2 = input("Ingrese los elementos del segundo conjunto: ")
        conjunto1 = Conjunto(elementos1.split(","))
        conjunto2 = Conjunto(elementos2.split(","))
        resultado = conjunto1 - conjunto2
        print("la diferencia de los conjuntos es:", resultado.elementos)
        
    elif opcion == 3:
        elementos1 = input("Ingrese los elementos del primer conjunto separados por coma: ")
        elementos2 = input("Ingrese los elementos del segundo conjunto separados por coma: ")
        conjunto1 = Conjunto(elementos1.split(","))
        conjunto2 = Conjunto(elementos2.split(","))
        if conjunto1 == conjunto2:
            print("Los conjuntos son iguales")
        else:
            print("Los conjuntos son diferentes")
            
    elif opcion == 4:
        return False
    
    else:
        print("Opción inválida, por favor seleccione una opción válida")
    
    return True

while menu():
    pass
