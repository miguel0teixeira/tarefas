tempAtividadeA = int (input ("informe o tempo em dias para a atividade A: "))
tempAtividadeb = int (input ("informe o tempo em dias para a atividade B: "))
tempAtividadec = int (input ("informe o tempo em dias para a atividade C: "))
soma = 0

if tempAtividadeA < 0 or tempAtividadeb < 0 or tempAtividadec < 0:
    print ("Os dias não podem ser negativos")
else:
    soma = tempAtividadeA + tempAtividadeb + tempAtividadec
    print(f"O tempo total é de {soma} dias")
