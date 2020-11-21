'''
This proyect is under GPL-3.0 License

@Authors:
	Juan Luis Ruiz Vanegas    ->  juanluisruiz971@gmail.com
	Brian Kalid Garcia Olivo  ->  briankalid2000@gmail.com
'''

import database
import processing

#cnx_morelia=database.morelia()
#cnx_patzcuaro=database.patzcuaro()

#print(processing.prueba(cnx_morelia))


#--- Menu ---#
def sucursal():
	#Mostrar sucursales
	print ('\n\t Bienvenido \n\t Selecciona tu sucursal \n\t 1.- Morelia \n\t 2.-Patzcuaro ')

	try:
		sucursal =  int(input())
		if (sucursal<1 or sucursal>2):
			print('Opcion invalida')
		else: return ( sucursal )
	except:
		print('Opcion invalida'


def operacion():
	print('\n\t \n\t Opciones: \n\t\t 1.- Insertar nuevos clientes y direcciones \n\t\t')
	print('\n\t\t 2.- Actualizar datos de los clientes y direcciones \n\t\t')
	print('\n\t\t 3.- Buscar Clientes por nombre, RFC, o domicilio desde cualquier sucursal \n\t\t')

	try:
		operacion = int(input())
		if (operacion<1 or operacion>3):
			print('Opcion invalida')
		else: return ( operacion )
	except:
		print('Opcion invalida')
	

sucursal = sucursal()
operacion =  operacion()

	
