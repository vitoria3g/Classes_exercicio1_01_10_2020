#01/10/2020 - Exercicio 1

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_salario(self):
        return self.__salario

    def set_nome(self):
        self.__nome = nome
    
    def set_cpf(self):
        self.__cpf = cpf
    
    def set_salario(self,salario):
        self.__salario = salario
    
    
func1 = Funcionario("Pedro", "111222333-22", 1500.0)
func1.set_salario(2000.0)              # Altera o salário
print("Nome:", func1.get_nome())
print("CPF:", func1.get_cpf())
print("Salário:", func1.get_salario())

