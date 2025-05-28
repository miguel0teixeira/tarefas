temperatura = int(input("informe a temperatura da sala "))

if temperatura > 30:
    print("muito quente, necessario resfriamento")
elif temperatura < 10:
    print("muito fria, necessario aqueciemento")
else:
    print("temperatura ideal")