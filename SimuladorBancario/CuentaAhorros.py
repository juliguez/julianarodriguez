class CuentaAhorro:
    # Aqui el codigo de cuenta de ahorro 
    # Atributos 
    saldo = 0
    InteresMensual = 0    
    '''_______________________________________________
    __________________________________________________
    #Metodos 
    __________________________________________________
    __________________________________________________'''
def ConsignarValor (self):
    nsaldo = self.saldo + 100000
    self.saldo = nsaldo
    return " El nuevo saldo mas el valor condignado es " + self.saldo

def RetirarValor (self):
    nsaldo = self.saldo - 100000
    self.saldo = nsaldo
    return " El nuevo saldo menos el valor retirado es " + self.saldo

def InteresMensual (self):
    nsaldo = self.saldo * 0.6
    nsaldo = self.saldo + nsaldo
    self.saldo = nsaldo
    return " El nuevo saldo mas el interes mensual es " + self.saldo