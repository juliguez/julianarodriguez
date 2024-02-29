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

    def ConsignarCuentaCorriente (self, ValorConsignacion):
        # Aqui el codigo del metodo
        # foma 1 
        self.CuentaCorriente.saldo += self.ConsignarCuentaCorriente(self.saldo)
        return "Usted ha condignado" + ValorConsignacion
        # forma 2
        # return self.CuentaCorriente.ConsignarValor()
    
    def CalcularSaldoTotal (self):
        #Aqui el codigo del metodo
        # forma 1
        Saldototal = self.CuentaCorriente + self.CuentaAhorros + self.CDT

        return "CalcularSaldoTotal:" 
    
    def PasardeCuentaAhorroaCuentaCorriente (self):
        # Aqui el codigo del metodo
        self.CuentaAhorros.saldo += self.CuentaCorriente.saldo
        self.CuentaAhorros.saldo = 0
        return "El saldo ha sido transferido" 
    
    def ConsultarSaldoCorriente (self):
        # Aqui va el codigo del metodo 
        return self.CuentaCorriente.saldo()
    
    def RetirarTodo (self):
        # Aqui va el codigo del metodo
        return "Dinero retirado con exito" +(self.CuentaCorriente.saldo + self.CuentaAhorros.saldo + self.CDT)
    
    def DuplicarAhorro (self):
        # Aqui el codigo del metodo
        nahorro = self.CuentaAhorros.saldo *2
        return "Su ahorro es" + nahorro
    
    
