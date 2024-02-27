class Empleado:
    # Aqui el copdigo}
    # Atributos
    Nombre = ""
    Apellido = ""
    Sexo = ""
    # 1= masculino 2= femenino
    Salario = 0
    '''---------------------------------------------------
    ------------------------------------------------------'''
    # Metodos 
    def CambiarSalario(self, nuevoSalario):
    # Aqui va el codigo del metodo 
        return 0

    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
    # Aqui va el codigo del nuevo Empleado
        return None 
        
    def ConsultarSalario(self):
    # Aqui va el codigo del metodo
        return self.Salario
    
    def ConsultarNombre(self):
    # Aqui va el codigo del metodo
        return self.Nombre
    
    def ConsultarApellido(self):
    # Aqui va el codigo del metodo
        return self.Apellido
    
    def ConsultarNombrecompleto(self):
    # Aqui va el codigo del metodo
        return self.Nombre +" "+ self.Apellido
    
        JulianaRodriguez
    
    def AumentoSalarial(self):
        nSalario = self.Salario = 0.05
        nSalario = nSalario + self.Salario
        self.Salario = nSalario
        return "El nuevo salario es de:"+self.Salario
