nota1=float(input("Digite a nota 1: "))
nota2=float(input("Digite a nota 2: "))
nota3=float(input("Digite a nota 3: "))
nota4=float(input("Digite a nota 4: "))
nota5=float(input("Digite a nota 5: "))

media=(nota1+nota2+nota3+nota4+nota5)/5

print("Sua média é ", media)
if media>=6:
    print(f"VOCÊ FOI APROVADO COM MÉDIA = {media}")
else:
    print(f"VOCÊ NÃO FOI APROVADO COM MÉDIA = {media}")