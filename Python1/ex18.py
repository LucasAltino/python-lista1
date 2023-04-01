f = int(input("Digite a quantidade de fitas da locadora: "))
a = float(input("Digite o valor do aluguel por fita: "))

print("Faturamento anual: ", ((f*a)/3)*12)
print("Valor ganho com multas por mês: ", ((f*a)/3)*0.01)
print("Quantidade de fitas que a locadora terá no final do ano: ", (f-(f*0.02)+(f*0.1)))