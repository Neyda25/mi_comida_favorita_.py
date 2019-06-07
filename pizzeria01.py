print("Bienvenido a la pizzeria")
pizzas = ["Pizza de peperoni", "Pizza cuatro estaciones", "Pizza borde rellenos", "Pizza hawaiana", "Pizza cuatro quesos", "Pizza de jamon y peperoni"]

def imprimir_menu():
	print("1 Mostrar Pizza")
	print("2 Eliminar pizzas")
	print("3 Agregar pizza")
	print("4 salir")
	valor = input("Ingrese el valor de la accion: ")
	return valor
	
def mostrar_pizza():
	for pizza in pizzas:
		print(pizza)

def eliminar_pizzas():
	pizzas = []

def agregar_pizza(valor):
	pizza.append(valor)
	
continuar = True

while continuar:
	#v_retornado = Valor Retornado
	v_retornado = imprimir_menu()
	if int(v_retornado) == 1:
		mostrar_pizza()
	elif int(v_retornado) == 2:
		eliminar_pizzas()
	elif int(v_retornado) == 3:
		valor = input("Ingrese la pizza a agregar: ")
		agregar_pizza(valor)
		pizza.append(valor)
	elif int(v_retornado) == 4:
		continuar = False
		eliminar_pizzass()
	else:
		print("Opcion no controlada")