def menu():

    print('CONVERSION DE UNIDADES TERMOMETRICAS')
    print('1. Grados Celcius')
    print('2. Fahrenheit')
    print('3. kelvin ')
    print('4. Rankine')
    opciones()

def opciones():

        opc = int(input('Digite una opcion: '))

        if (opc >=1 and opc <=4):

            if(opc == 1):
                celsius=float(input('Ingrese los grados celcius: '))
                fahrenheit=celsius*(9/5)+(32)
                kelvin= celsius+(273)
                rankine=celsius*(9/5)+(491.67)
                print(str(celsius)+' °C equivale a:\n\n'+str(fahrenheit)+'°F')
                print(str(kelvin)+'°K')
                print(str(rankine)+'°R')

            if(opc == 2):
                fahrenheit = float(input('Ingrese grados Fahrenheit: '))
                celsius=(fahrenheit-32)*(5/9)
                kelvin=(5/9)*(fahrenheit-32)+(273)
                rankine=fahrenheit+(459)
                print(str(fahrenheit)+'°F equivale a:\n\n'+str(celsius)+'°C')
                print(str(kelvin)+'K')
                print(str(rankine)+'R')
            if (opc==3):
                kelvin = float(input('Ingrese grados kelvin:\n '))
                celsius=(kelvin-273)*(9/5)+(32)
                fahrenheit= (9/5)*(k-273)+(491)
                print(str(kelvin)+'°K equivale a :\n\n'+str(celsius)+'°C')
                print(str(fahrenheit)+'°F')
                print(str(rankine)+'°R')
            if(opc==4):
                rankine=float(input('Ingrese grados Rankine: '))
                celsius=(rankine-491)*(5/9)
                kelvin=(rankine-491)*(5/9)+273
                fahrenheit=rankine-459
                print(str(rankine)+'°R equivale a:\n\n'+str(celsius)+'°C')
                print(str(fahrenheit)+'°F')
                print(str(kelvin)+'°K ')

            mostrar_nuevamente()
        else:
            print('\nError se ha digitado una opcion no valida')


def mostrar_nuevamente():

        decision = input( '\n¿Desea Realizar otra conversion?  ¿Si/No?: ')

        while decision =='si'or decision =='SI'or decision=='Si':
            return menu()

menu()