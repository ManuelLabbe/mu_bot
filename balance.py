class balance:
    def __init__(self, valor_real: int):
        self.saldo_actual = 0
        self.valor_real = valor_real 
    def deposito(self, valor_deposito: int):
        self.saldo_actual += valor_deposito
        self.porcentaje = (self.saldo_actual / self.valor_real) * 100