plano=100
min=int(input("Digite a quantidade de minutos: "))
min_excedentes=min-plano
valor_excedente=min_excedentes*2

if min <=100:
    print ("Valor a pagar: R$50.00")
elif min >100:
    print(f"Valor a pagar: R${valor_excedente+50}.00")