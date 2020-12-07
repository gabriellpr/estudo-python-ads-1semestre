import conta

conta1 = conta.Conta('Joao', 1)
conta1.Depositar(200)

conta2 = conta.Conta('Maria', 2)
conta2.Depositar(300)

conta1.transferencia(conta2, 100)

print(conta1.saldo())
print(conta1.getCliente())
