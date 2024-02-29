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
        Saldototal = self.saldo 
        return "CalcularSaldoTotal:" 
    
    def PasardeCuentaAhorroaCuentaCorriente (self):
        # Aqui el codigo del metodo
        return 
    
    def ConsultarSaldoCorriente (self):
        # Aqui va el codigo del metodo 
        return self.CuentaCorriente.saldo()
    
    def RetirarTodo (self):
        # Aqui va el codigo del metodo
        return "Dinero retirado con exito" +(self.CuentaCorriente.saldo + self.CuentaAhorros.saldo + self.CDT)
    
