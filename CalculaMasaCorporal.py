def calculamasacorporal():

    print("\nCALCULO MASA CORPORAL\n")
    try:
        edad=int(input('Ingrese su edad: '))
    except ValueError:
       print('El dato que ingreso no es valido')
       return 0

    altura=float(input('Ingrese su altura: '))
    peso=float(input('Ingrese su peso: '))
    imc=peso/(pow(altura,2))

    if edad <45 and imc<22:
        print("\nEl indice de masa corporal es: inferior al normal")
    elif edad<45 and imc>22:
        print('\nEl indice de masa corporal es: normal')
    elif edad>=45 and imc<22:
        print('\nEl indice de masa corporal es: superior medio')
    else:
        print('\nEl indice de masa corporal es: obesidad')

calculamasacorporal()

