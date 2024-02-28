class CuentaCorriente:
    # Aqui el codigo
    # Atributos
    saldo = 0

    '''---------------------------------------------------
    # Metodos
    ------------------------------------------------------'''

    def ConsignarValor (self):
        nsaldo = self.saldo + 150000
        self.saldo = nsaldo
        return " El nuevo saldo mas el valor consignado es " + self.saldo
    
    def RetirarValor (self):
        nsaldo = self.saldo - 150000
        self.saldo = nsaldo
        return " El nuevo saldo menos el valor retirado es " + self.saldo
    