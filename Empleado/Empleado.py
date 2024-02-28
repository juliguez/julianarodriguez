class empleado:
    # Aqui el codigo
    # Atributos
    nombre = ""
    apellido = ""
    sexo = ""
    # 1= masculino 2= femenino
    salario = 0

    '''---------------------------------------------------
    # Metodos
    ------------------------------------------------------'''

    def CambiarSalario(self, nuevosalario):
    # Aqui va el codigo del metodo 
        return 0

    def CambiarEmpleado(self, nnombre, napellido, nsexo, nsalario):
    # Aqui va el codigo del nuevo Empleado
        return None 
        
    def ConsultarSalario(self):
    # Aqui va el codigo del metodo
        return self.salario
    
    def ConsultarNombre(self):
    # Aqui va el codigo del metodo
        return self.nombre
    
    def ConsultarApellido(self):
    # Aqui va el codigo del metodo
        return self.apellido
    
    def ConsultarNombrecompleto(self):
    # Aqui va el codigo del metodo
        return self.nombre +" "+ self.apellido
    
        JulianaRodriguez
    
    def AumentoSalarial(self):
        nsalario = self.salario = 0.05
        nsalario = nsalario + self.salario
        self.salario = nsalario
        return "El nuevo salario es de:"+self.salario

    def DuplicarSalario (self):
        # Aqui va el codigo 
        # Forma 1
        self.salario = self.salario*2
        # Forma 2
        self.salario *= 2

    def CalcularSalarioAnual (self):
        # Aqui va el codigo 
        asalario = self.salario * 12
        return asalario

