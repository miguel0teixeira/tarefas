nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >=7:
    print("Aprovado")
elif 5<= media < 7:
    print("Recuperação")
else:
    print("Reprovado")
