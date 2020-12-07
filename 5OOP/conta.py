class Conta:
  def __init__(self, nome, numero):
    self.cliente = nome
    self.num = numero
    self.saldo = 0

  def saldo(self):
    return self.saldo

  def getCliente(self):
    return self.cliente
  
  def Depositar(self, valor):
    self.saldo += valor

  def transferencia(self, conta, valor):
    self.saldo = self.saldo - valor
    conta.saldo = conta.saldo + valor



