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

sucursales,cnxs = database.init_databases()
print(sucursales,cnxs)


#--- Menu ---#
def Sucursal():
    #Mostrar sucursales
    print ('\n\t Bienvenido \n\t Selecciona tu sucursal\n')
    for i in range (len(sucursales)):
        print("\t",i+1,".-", sucursales[i])
    
    try:
        sucursal =  int(input())
        if (sucursal<1 or sucursal>len(sucursales)):
            print("< OPCION INVALIDA >")
        else: return ( sucursal )
    except:
        print("< OPCION INVALIDA >")


def Operacion():
    print('\n\t \n\t Opciones: \n\t\t 1.- Insertar nuevos clientes y direcciones \n\t\t')
    print('\n\t\t 2.- Actualizar datos de los clientes y direcciones \n\t\t')
    print('\n\t\t 3.- Buscar Clientes por nombre, RFC, o domicilio desde cualquier sucursal \n\t\t')

    try:
        operacion = int(input())
        if (operacion<1 or operacion>3):
            print("< OPCION INVALIDA >")
        else: return ( operacion )
    except:
        print("< OPCION INVALIDA >")

def Buscar_cliente():
    print ("\n\t Buscar cliente por: \n 1.- Nombre \n 2.- RFC \n 3.- Domicilio")
    try: 
        opcion_busqueda = int(input())
        if (opcion_busqueda<1 or opcion_busqueda>3):
            print("< OPCION INVALIDA >")
        else: return(opcion_busqueda)
    except: 
        print("< OPCION INVALIDA >")
        

def Datos_registrar_cliente():
    datos = []
    print("\n\t Nombre: ")
    NOMBRE = input()
    print("\n\t Apellido Paterno: ")
    AP = input()
    print("\n\t Apellido Materno: ")
    AM = input()
    print("\n\t RFC: ")
    RFC = input()
    print("\n\t Calle: ")
    CALLE = input()
    print("\n\t Colonia: ")
    COLONIA = input()
    print("\n\t Estado: ")
    ESTADO = input()
    print("\n\t Codigo Postal: ")
    CP = input()
    
    return (NOMBRE, AP, AM, RFC, CALLE, COLONIA, ESTADO, CP)


sucursal = Sucursal()

if (sucursal == 1):   
    sucursal = "Morelia"
    operacion =  Operacion()
    
    if operacion == 1:
        #def registrar_cliente(cnx,nombre,ap,am,rfc,calle,col,est,cp)
        #Checar si los datos a dar de alta ya esta en algunda de las db
        NOMBRE, AP, AM, RFC, CALLE, COLONIA, ESTADO, CP = Datos_registrar_cliente()
        
        if( not processing.inDatabase(sucursales,cnxs,NOMBRE,AP,AM,RFC) ): #if not in databases
            #Dar de alta 
            processing.registrar_cliente(cnxs[0],NOMBRE, AP, AM, RFC, CALLE, COLONIA, ESTADO, CP)
        
    #elif operacion == 2:
        #Actualizar datos
    
    elif operacion == 3:
        #buscar clientes
        opcion_busqueda = Buscar_cliente()
        #if opcion_busqueda == 1: #Por nombre
        
elif (sucursal == 2): 
    sucursal = "Patzcuaro"
    operacion =  Operacion()
    if operacion == 1:
        #def registrar_cliente(cnx,nombre,ap,am,rfc,calle,col,est,cp)
        #Checar si los datos a dar de alta ya esta en algunda de las db
        NOMBRE, AP, AM, RFC, CALLE, COLONIA, ESTADO, CP = Datos_registrar_cliente()
        
        if( not processing.inDatabase(sucursales,cnxs,NOMBRE,AP,AM,RFC) ): #if not in databases
            #Dar de alta 
            processing.registrar_cliente(cnxs[1],NOMBRE, AP, AM, RFC, CALLE, COLONIA, ESTADO, CP)
        
    #elif operacion == 2:
        #Actualizar datos
    
    elif operacion == 3:
        #buscar clientes
        opcion_busqueda = Buscar_cliente()
        #if opcion_busqueda == 1: #Por nombre
    
