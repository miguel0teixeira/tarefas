horario = int(input("digite a hora atual: "))

if horario > 18 or horario < 8:
    print("acesso negado pelo horario")
else:
    print("acesso liberado")