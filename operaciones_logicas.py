class OperacionesLogicas:
    def __init__(self):
        self.operadores = {
            '^': self.conjuncion,
            'v': self.disyuncion,
            '⊻': self.disyuncion_excluyente,
            '→': self.condicional,
            '↔': self.bicondicional
        }

    def conjuncion(self, p, q):
        return p and q

    def disyuncion(self, p, q):
        return p or q

    def disyuncion_excluyente(self, p, q):
        return (p or q) and not (p and q)

    def condicional(self, p, q):
        return not p or q

    def bicondicional(self, p, q):
        return (not p or q) and (not q or p)