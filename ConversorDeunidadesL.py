def pulgadasaMilimetros():
    pulgadas=int(input("Ingrese la cantidad de pulgadas a convertir: "))
    milimetros=pulgadas*25.40
    print(pulgadas," pulgadas equivalen a: ",milimetros," milimetros")


def yardasaMetros():
    yardas = int(input("Ingrese la cantidad de yardas a convertir: "))
    metros = yardas * 0.9144
    print(yardas, " yardas equivalen a: ", metros, " milimetros")

def millasakilometros():
    millas = int(input("Ingrese la cantidad de millas a convertir: "))
    kilometros = millas * 1.6093
    print( millas," millas equivalen a: ", kilometros, " milimetros")


opc = int (input('MENU\n\n1.Pulgadas a milimetros\n2.Yardas a metros\n3.Millas a kilometros\n\nIngrese una opcion: '))
diccionario = {1:pulgadasaMilimetros, 2:yardasaMetros, 3:millasakilometros}
try:
    diccionario[opc]()
except:
    print("opcion no valida")