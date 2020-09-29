class Calcula:
	descision=False
	def suma(x,y):
		return x + y

	def resta(x,y):
		return x-y

	def multiplicacion(x,y):
		return x*y

	def division(x,y):
		return x/y

def menu():
	print("\tCALCULADORA\n")
	print("1.SUMA")
	print("2.RESTA")
	print("3.MULTIPLICACION")
	print("4.DIVISION")

	opcion = int(input("\nINGRESA UNAOPCION: "))
	if (opcion >=1 and opcion <=4):
		num1 = int(input("Ingresa un número: "))
		num2 = int(input("Ingresa otro número: "))

		if opcion == 1:
			print(num1,"+",num2,"=", Calcula.suma(num1,num2))
		elif opcion == 2:
			print(num1,"-",num2,"=", Calcula.resta(num1,num2))
		elif opcion == 3:
			print(num1,"*",num2,"=", Calcula.multiplicacion(num1,num2))
		elif opcion == 4:
			print(num1,"/",num2,"=", Calcula.division(num1,num2))

	else:
		print("Entrada invalida!!")


	print("\nDesea realizar otra operacion?")

	descision=input("Si/No?: ")

	if (descision=='Si' or descision=='si' or descision=='SI'):
		descision=True
	elif(descision=='No'or descision=='no'or descision=="NO"):
		descision=False
	while(descision==True):
		menu()
menu()


