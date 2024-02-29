from CDT import CDT
from CuentaAhorros import CuentaAhorro
from CuentaCorriente import CuentaCorriente

class SimuladorBancario:
    # Aqui va el codigo
    # Atributos
    Cedula = ""
    Nombre = ""
    MesActual = ""

    '''---------------------------------------------------
    # Asociaciones
    ------------------------------------------------------'''

    CuentaCorriente = CuentaCorriente()
    CuentaAhorros = CuentaAhorro()
    CDT = CDT()

    '''---------------------------------------------------
    # Metodos
    ------------------------------------------------------'''

    def ConsignarCuentaCorriente (self):
        # Aqui el codigo del metodo
        return self.CuentaCorriente.ConsignarValor()
    
    def CalcularSaldoTotal (self):
        #Aqui el codigo del metodo
        return "CalcularSaldoTotal:" +(self.CuentaCorriente.saldo + self.CuentaAhorros.saldo)
    
    def PasardeCuentaAhorroaCuentaCorriente (self):
        # Aqui el codigo del metodo
        return 
