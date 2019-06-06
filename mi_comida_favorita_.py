comidas = ["Ensalada Templada", "Papas Fritas", 
"Paella De Mariscos", "Tacos Mexicanos", 
"Pollo A La Parmesana", "Lasaña", "Omelet", 
"Sopa Marinera", "Camarones Empanizados", 
"Hamburguesa", "Sandwiches", "Caldo De Pollo", 
"Arroz Con Pollo", "Pollo En Salsa De Hongos",
"Omelet De Papa", "Pastel De Papas", "Bistec De Res",
"Pizza", "Pollo Al Horno", "Baledas"]

comidas_favoritas = ["Lasaña", "Sandwiches", 
"Pastel De Papas", "Pizza", "Bistec De Res"]

def imprimir_menu():
	print("escoge dos de las siguentes comidas: ")
	for comida in comidas:
		print(comida)
	print("Estas son mis cinco comidas favoritas: ")
	for comida in comidas_favoritas:
		print(comida)		
		
imprimir_menu()
