class CuentaCorriente:
    # Aqui el codigo
    # Atributos
    saldo = 0

    '''---------------------------------------------------
    # Metodos
    ------------------------------------------------------'''
    def ConsultarSaldo (self):
        # Aqui va el codigo del metodo
        return self.saldo

    def ConsignarValor (self,saldo):
        nsaldo = self.saldo + 150000
        self.saldo = nsaldo
        return " el valor consignado es " + ""
    
    def RetirarValor (self,saldo):
        nsaldo = self.saldo - 150000
        self.saldo = nsaldo
        return " el valor retirado es " + ""
    
    # control kc
    # cpntrol ku