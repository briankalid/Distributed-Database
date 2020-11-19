'''
This proyect is under GPL-3.0 License

@Authors:
	Juan Luis Ruiz Vanegas    ->  juanluisruiz971@gmail.com
	Brian Kalid Garcia Olivo  ->  briankalid2000@gmail.com
'''

import database
import processing

cnx_morelia=database.morelia()
cnx_patzcuaro=database.patzcuaro()

print(processing.prueba(cnx_morelia))
