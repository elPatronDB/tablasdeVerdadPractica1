from operaciones_logicas import OperacionesLogicas

class TablaVerdad:
    def __init__(self):
        self.variables = []
        self.expresiones = []
        self.op_logicas = OperacionesLogicas()
        self.conectores = {
            '1': ('^', 'Conjunción (AND)'),
            '2': ('v', 'Disyunción (OR)'),
            '3': ('⊻', 'Disyunción Excluyente (XOR)'),
            '4': ('→', 'Condicional (IMPLICA)'),
            '5': ('↔', 'Bicondicional (SI Y SOLO SI)')
        }

    def mostrar_conectores(self):
        print('\nSeleccione un conector lógico:')
        for key, (simbolo, descripcion) in self.conectores.items():
            print(f'{key}. {descripcion} ({simbolo})')
        while True:
            try:
                opcion = input('Ingrese el número del conector: ').strip()
                if opcion not in self.conectores:
                    raise ValueError('Opción inválida.')
                return self.conectores[opcion][0]  # Devuelve el símbolo (ej. '^')
            except ValueError as e:
                print(f'Error: {e}. Intente de nuevo.')

    def ingresar_datos(self):

        while True:
            try:
                entrada = input('Ingrese variables (1-3) separadas por comas').replace(' ', '').lower()
                if not entrada:
                    raise ValueError('Ingrese una variable como mínimo')
                variable_input = entrada.split(',')
                if not (1 <= len(variable_input) <= 3):
                    raise ValueError('Debe ingresar entre 1 y 3 variables')
                for variable_s in variable_input:
                    if not (len(variable_s) == 1 and variable_s.isalpha()):
                        raise ValueError(f''{variable_s}' no puede usarse como variable, se recomienda usar letras')
                self.variables = variable_input
                break
            except ValueError as e:
                print(f'Error: {e}. Intente de nuevo.')

        while True:
            try:
                n_expresiones = int(input('¿Cuántas expresiones desea ingresar (1-3)? '))
                if not (1 <= n_expresiones <= 3):
                    raise ValueError('Debe ser entre 1 y 3.')
                self.expresiones = []
                for i in range(n_expresiones):
                    print(f'\nExpresión {i+1}:')
                    tipo = input('¿Es una variable sola (s) o una expresión con conector (c)? ').lower()
                    if tipo == 's':
                        variable_s = input('Ingrese la variable: ').lower()
                        if len(variable_s) != 1 or not variable_s.isalpha() or variable_s not in self.variables:
                            raise ValueError(f''{variable_s}' no es válida o no está en las variables ingresadas.')
                        self.expresiones.append(variable_s)
                    elif tipo == 'c':
                        variable_s1 = input('Ingrese la primera variable: ').lower()
                        if len(variable_s1) != 1 or not variable_s1.isalpha() or variable_s1 not in self.variables:
                            raise ValueError(f''{variable_s1}' no es válida o no está en las variables ingresadas.')
                        conector = self.mostrar_conectores()
                        variable_s2 = input('Ingrese la segunda variable: ').lower()
                        if len(variable_s2) != 1 or not variable_s2.isalpha() or variable_s2 not in self.variables:
                            raise ValueError(f''{variable_s2}' no es válida o no está en las variables ingresadas.')
                        self.expresiones.append(variable_s1 + conector + variable_s2)
                    else:
                        raise ValueError('Responda 's' para variable sola o 'c' para conector.')
                break
            except ValueError as e:
                print(f'Error: {e}. Intente de nuevo.')

    def validar_expresiones(self, expresiones):
        operadores = ['^', 'v', '⊻', '→', '↔']
        for expr in expresiones:
            if len(expr) > 3 or (len(expr) == 3 and expr[1] not in operadores):
                return False
            variable_input_en_expr = [c for c in expr if c.isalpha()]
            if len(variable_input_en_expr) > 2:
                return False
            for var in variable_input_en_expr:
                if var not in self.variables:
                    return False
        return True

    def generar_tabla(self):
        n_variable_input = len(self.variables)
        combinaciones = []
        for i in range(2 ** n_variable_input):
            fila = [int(bit) for bit in format(i, f'0{n_variable_input}b')]
            combinaciones.append(fila)

        encabezado = ' | '.join(self.variables + self.expresiones)
        print('---- Se ha generado la siguiente tabla de verdad ----')
        print(f'| {encabezado} |')
        print('|' + '-' * (len(encabezado) + 2) + '|')

        for fila in combinaciones:
            valores = dict(zip(self.variables, fila))
            resultados = []
            for expr in self.expresiones:
                if len(expr) == 1:
                    res = valores[expr]
                else:
                    p, op, q = expr[0], expr[1], expr[2]
                    res = self.op_logicas.operadores[op](valores[p], valores[q])
                resultados.append(int(res))
            fila_str = ' | '.join([str(v) for v in fila + resultados])
            print(f'| {fila_str} |')