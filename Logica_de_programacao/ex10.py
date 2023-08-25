glicose= float(input("Digite a quantidade de glicose: "))

if glicose<=100:
    print("Classificação: normal")
elif glicose>100 and glicose<=140:
    print("Classificação: elevado")
elif glicose>140:
    print("Classificação: diabetes")
