'''
This proyect is under GPL-3.0 License

@Authors:
	Juan Luis Ruiz Vanegas    ->  juanluisruiz971@gmail.com
	Brian Kalid Garcia Olivo  ->  briankalid2000@gmail.com
'''

import database
import processing


sucursales,cnxs = database.init_databases()


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
    print('\n\t\t 4.- Salir \n\t\t')

    try:
        operacion = int(input())
        if (operacion<1 or operacion>4):
            print("< OPCION INVALIDA >")
        else: return ( operacion )
    except:
        print("< OPCION INVALIDA >")

def Buscar_cliente(up=None):

    if up:
        print ("\n\t Buscar cliente por: \n 1.- Nombre \n 2.- RFC \n 3.- Domicilio")
        try: 
            opcion_busqueda = int(input())
            if (opcion_busqueda<1 or opcion_busqueda>3):
                print("< OPCION INVALIDA >")
            else: return(opcion_busqueda)
        except: 
            print("< OPCION INVALIDA >")
 

    else:
        print ("\n\t Buscar cliente por: \n 1.- Nombre \n 2.- RFC \n 3.- Domicilio \n 4.- Listado Completo")
        try: 
            opcion_busqueda = int(input())
            if (opcion_busqueda<1 or opcion_busqueda>4):
                print("< OPCION INVALIDA >")
            else: return(opcion_busqueda)
        except: 
            print("< OPCION INVALIDA >")
            

if __name__=='__main__':
    #primero necesitamos saber de que sucursal es
    SERVICE_ON = True
    sucursal = Sucursal() 
    while SERVICE_ON:
        operacion =  Operacion()
        
        if operacion == 1:
            #Checar si los datos a dar de alta ya esta en algunda de las db
            NOMBRE=input("\n\t Nombre: ")
            AP=input("\n\t Apellido Paterno: ")
            AM=input("\n\t Apellido Materno: ")
            RFC=input("\n\t RFC: ")
            
            if( not processing.inDatabase(sucursales,cnxs,NOMBRE,AP,AM,RFC) ): #if not in databases
                #Dar de alta 
                CALLE=input("\n\t Calle: ")
                COLONIA=input("\n\t Colonia: ")
                ESTADO=input("\n\t Estado: ")
                CP=input("\n\t Codigo Postal: ")
                processing.registrar_cliente(cnxs[sucursal-1],NOMBRE, AP, AM, RFC, CALLE, COLONIA, ESTADO, CP)
            
        elif operacion == 2:
            #2.- Actualizar datos de los clientes y direcciones
            opcion_busqueda = Buscar_cliente(up=True)
            if opcion_busqueda == 1: #Por nombre
                NOMBRE = input('\n\t Nombre: ')
                AP = input('\n\t Apellido Paterno: ')
                AM = input('\n\t Apellido Materno: ')
                processing.buscar_cliente(cnxs,nombre=NOMBRE,ap=AP,am=AM)
                
            elif opcion_busqueda == 2: #Por RFC
                RFC = input('\n\t RFC: ')
                processing.buscar_cliente(cnxs,RFC)
                
            elif opcion_busqueda == 3: #Por Direccion
                CALLE = input("\n\t Calle: ")
                COLONIA = input("\n\t Colonia: ")
                ESTADO=input("\n\t Estado: ")
                CP=input("\n\t Codigo Postal: ")
                processing.buscar_cliente(cnxs,calle=CALLE,colonia=COLONIA,estado=ESTADO,cp=CP)
                
             
        elif operacion == 3:
            #buscar clientes
            opcion_busqueda = Buscar_cliente()
            if opcion_busqueda == 1: #Por nombre
                NOMBRE = input('\n\t Nombre: ')
                AP = input('\n\t Apellido Paterno: ')
                AM = input('\n\t Apellido Materno: ')
                processing.buscar_cliente(cnxs,nombre=NOMBRE,ap=AP,am=AM)
                
            elif opcion_busqueda == 2: #Por RFC
                RFC = input('\n\t RFC: ')
                processing.buscar_cliente(cnxs,RFC)
                
            elif opcion_busqueda == 3: #Por Direccion
                CALLE=input("\n\t Calle: ")
                COLONIA=input("\n\t Colonia: ")
                ESTADO=input("\n\t Estado: ")
                CP=input("\n\t Codigo Postal: ")
                processing.buscar_cliente(cnxs,calle=CALLE,colonia=COLONIA,estado=ESTADO,cp=CP)
                
            elif opcion_busqueda == 4: #Listado Completo
                processing.all_client(sucursales,cnxs)
                
        elif operacion == 4: 
            SERVICE_ON = False
                    
