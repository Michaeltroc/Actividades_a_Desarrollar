def decimalabinario():
   numero =int(input("Ingrese un numero: "))
   convertido= bin(numero)[2:]
   print(convertido)


def decimalaoctal():
    numero = int(input("Ingrese un numero: "))
    convertido = oct(numero)[2:]
    print(convertido)

def decimalahexadecimal():
    numero = int(input("Ingrese un numero: "))
    convertido = hex(numero)[2:]
    print(convertido)


print('CONVERSOR DE NUMEROS A DECIMALES')
opc = int(input('MENU\n\n1.decimal a binario\n2.decimal a octal\n3.decimal a hexadecimal\n\nIngrese una opcion:'))
diccionario ={1:decimalabinario, 2:decimalaoctal,3:decimalahexadecimal}
try:
    diccionario[opc]()
except:
    print('opcion no valida')