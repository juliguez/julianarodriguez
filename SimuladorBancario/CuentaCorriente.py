class CuentaCorriente:
    # Aqui el codigo
    # Atributos
    saldo = 0

    '''---------------------------------------------------
    # Metodos
    ------------------------------------------------------'''
    def ConsultarValor (self):
        # Aqui va el codigo del metodo
        return self.saldo

    def ConsignarValor (self,saldo):
        nsaldo = self.saldo + ""
        self.saldo = nsaldo
        return " el valor consignado es " + ""
    
    def RetirarValor (self,saldo):
        nsaldo = self.saldo - ""
        self.saldo = nsaldo
        return " el valor retirado es " + ""
    