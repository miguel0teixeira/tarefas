peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura em metros: "))

IMC = peso / (altura * 2)
print(f"seu IMC: {IMC:.2f}")

if IMC < 18.5:
    print("abaixo do peso")
elif IMC > 18.5  and IMC < 25:
    print("peso ideal")
else:
    print("acima do peso")