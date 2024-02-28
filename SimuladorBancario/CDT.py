class CDT:
    # Aqui va el codigo
    # Atributos
    ValorInversion = 0
    InteresMensual = 0
    MesApertura = ""
    '''__________________________________________________
    __________________________________________________'''
    #Metodos
    '''__________________________________________________
    __________________________________________________'''
    def InteresMensual (self):
        nsaldo = self.saldo * 0.0
        nsaldo = self.saldo + nsaldo
        self.saldo = nsaldo
        return " Su interes es " + self.saldo