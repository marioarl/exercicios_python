'''
Credito : https://wiki.python.org.br/ExerciciosClasses ref: Ex 5

Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque.
No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
'''
class ContaCorrente:
    def __init__(self,numero,nome,saldo=0):
        self.num = numero
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self,novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor

conta1 = ContaCorrente("202023", "Eurico da Silva")
print(f"Conta Corrente: {conta1.num}")
print(f"Nome..........: {conta1.nome}")
print(f"Saldo.........: {conta1.saldo}")
            

