class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def __pode_sacar(self, valor):
        if valor <= (self.__saldo + self.__limite):
            return True
        else:
            return False

    def extrato(self):
        print(self.__titular)
        print(self.__saldo)

    def deposita(self,valor):
        self.__saldo += valor
        print("Depósito realizado!")

    def saca(self,valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def lista_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

