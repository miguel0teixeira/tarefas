distanciaPercorrida = int(input("digite sua distancia percorrida em km: "))

if distanciaPercorrida < 10:
    print("10 reais")
elif 100 < distanciaPercorrida <= 200:
    print("20 reais")
else:
    print("30 reais")