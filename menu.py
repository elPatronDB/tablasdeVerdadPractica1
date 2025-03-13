import os
from tabla import TablaVerdad

class Menu:
    def __init__(self):
        self.tabla = TablaVerdad()

    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrarMenu(self):
        self.clearScreen()
        print('\nGENERADOR DE TABLAS DE VERDAD - DIEGO BRAN')
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
                input("\nPresiona Enter para continuar...")
                self.mostrarMenu()
            elif opcion == 2:
                print('¡ADIOS!')
            else:
                print('Solamente puede escribir una de las dos opciones (1 o 2)')
                self.mostrarMenu()
        except ValueError as problema:
            if str(problema) == 'No es posible la opción en blanco':
                print('Error: Debe ingresar una opción')
            else:
                print('Error: Ingrese un número válido (1 o 2)')
            self.mostrarMenu()
        except Exception as e:
            print(f'Error inesperado: {e}')
            self.mostrarMenu()

if __name__ == "__main__":
    menu = Menu()
    menu.mostrarMenu()