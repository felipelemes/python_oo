class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(self.titular)
        print(self.saldo)

    def deposita(self,valor):
        self.saldo += valor
        print("Depósito realizado!")

    def saca(self,valor):
        self.saldo -= valor
        print("Saque realizado!")

