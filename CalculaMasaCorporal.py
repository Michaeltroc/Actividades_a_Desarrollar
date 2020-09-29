def calculamasacorporal():

    print("\nCALCULO MASA CORPORAL\n")
    edad=int(input('Ingrese su edad: '))
    altura=float(input('Ingrese su altura: '))
    peso=float(input('Ingrese su peso: '))
    imc=peso/(pow(altura,2))

    if edad <45 and imc<22:
        print("\nEl indice de masa corporal es: bajo")
    elif edad<45 and imc>22:
        print('\nEl indice de masa corporal es: medio')
    elif edad>=45 and imc<22:
        print('\nEl indice de masa corporal es: medio')
    else:
        print('\nEl indice de masa corporal es: alto')

calculamasacorporal()

