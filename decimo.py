mensal = int(input("digite sua renda mensal: "))
parcela = int(input("digite o valor da parcela desejada: "))

if mensal > 2000 and parcela <= 0.3 * mensal:
    print("Emprestimo aprovado")
elif mensal <= 2000:
    print("emprestimo negado: renda insuficiente")
else:
    print("emprestimo negado: acima de 30 da procentagem de sua renda")
