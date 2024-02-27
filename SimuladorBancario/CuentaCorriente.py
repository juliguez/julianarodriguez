class CuentaCorriente:
    # Aqui el codigo
    # Atributos
    saldo= 0

    def ConsignarSaldo (self):
        nsaldo = self.saldo + 150000
        self.saldo = nsaldo
        return "El nuevo saldo mas el valor asignado es" + self.saldo