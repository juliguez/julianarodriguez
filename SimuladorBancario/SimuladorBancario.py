from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class SimuladorBancario:
    
    cedula=''
    nombres=''
    mesActual=''
    
    '''----------------------------------------------------------------
    # Asociaciones
    ----------------------------------------------------------------'''
    
    CuentaCorriente = CuentaCorriente()
    CuentaAhorros = CuentaAhorros()
    CDT = CDT()
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    def CalcularSaldoTotal(self):
        # Forma1
        return self.corriente.ConsultarSaldo()+self.ahorros.ConsultarSaldo()

        # #Forma2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # saldoCorriente = self.corriente.ConsultarSaldo()
        # return saldoAhorros+saldoCorriente
        
    def PasarAhorrosACorriente(self):
        # forma1
        # self.corriente.ConsignarMonto(self.ahorros.ConsultarSaldo())
        # self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())
        
        # forma 2
        # saldoAhorros = self.ahorros.ConsultarSaldo()
        # self.ConsignarCuentaCorriente(saldoAhorros)
        # self.ahorros.RetirarMonto(self, saldoAhorros)
        
        #forma 3
        saldoAhorros = self.ahorros.ConsultarSaldo()
        self.corriente.saldo += saldoAhorros
        self.ahorros.saldo = 0
        

    def RetirarTodo(self):
        total = self.CalcularSaldoTotal()
        self.CuentaCorriente.RetirarValor(self.CuentaCorriente.ConsultarSaldo)
        self.CuentaAhorros.RetirarValor(self.CuentaAhorros.ConsultarSaldo)
        return "retiraste total: "+total

            
   
        

        