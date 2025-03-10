from tabla import TablaVerdad
import os

class Menu:
    def __init__(self):
        self.tabla = TablaVerdad()

    def clearScreen(self):
        os.system('cls')

    def mostrarMenu(self):
        while True:
            print('\n               GENERADOR DE TABLAS DE VERDAD - DIEGO BRAN')
            print('\n1. Generar tabla de verdad')
            print('2. Salir')
            try:
                opcion = input('\nElige una opción: ').strip()
                if not opcion:
                    raise ValueError('No es posible la opción en blanco')
                opcion = int(opcion)
                if opcion == 1:
                    self.tabla.ingresar_datos()
                    self.tabla.generar_tabla()
                elif opcion == 2:
                    print('¡ADIOS!')
                    break
                else:
                    print('Solamente puede escribir una de las dos opciones')
            except ValueError as problema:
                if str(problema) == 'La opción no puede estar vacía':
                    print('Error: Debe ingresar una opción')
                else:
                    print('Error: Ingrese un número válido (1 o 2)')
        
