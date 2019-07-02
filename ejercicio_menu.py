menus = ["Lasagna", "Baleadas", "Tacos", "hamburguesa", "Sandwich"]

def imptimir_menu():
	print("1 Listar menu")
	print("2 Agregar Pedidio")
	print("3 Imprimir Pedidos")
	print("4 Salir")
	valor = input("Ingrese el valor de la accion: ")
	return valor

def listar_menu():
	print()
	print("Listado de Menu")
	for producto in range (len(menus)):
		print("{0} {1}".format(producto, menus[producto])
		

def Agregar Pedido(valor):
	print()
	print("creando un pedido")
	mesa = input("Numero de mesa")
	producto = input("Nombre de platillo")
	pedidos.append("Mesa No. {0} platillo {1}".format(mesa, producto))
	

def imprimir_pedidos():
	if pedidos:
		for pedido in pedidos:
			print(pedido)
	else:
		print("No hay pedidos ingresados")

continuar = True

while continuar:
	#v_retornado = Valor Retornado
	v_retornado = imprimir_menu()
	if int(v_retornado) == 1:
		listar_menu()
	elif int(v_retornado) == 2:
		mesa = input("Numero de mesa")
		producto = input("Nombre de platillo")
		agragar_pedido()
		pedidos.append("Mesa No. {0} platillo {1}".format(mesa, producto))
		
	elif int(v_retornado) == 3:
		imprimir pedidos()
	elif int(v_retornado) == 4:
		continuar = False
		eliminar_menus()
	else:
		print("Opcion no controlada")


