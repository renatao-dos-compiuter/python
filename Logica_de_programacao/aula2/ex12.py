valor_uni=(float(input("Digite o valor unitário do produto: ")))
quantidade=(float(input("Digite a quantidade comprada do produto: ")))
dinheiro= (float(input("Digite o valor recebido: ")))

if dinheiro<valor_uni*quantidade:
    print(f"DINHEIRO INSUFICIENTE! FALTAM R${valor_uni*quantidade-dinheiro} REAIS")

else:
    print(f"TROCO: R${dinheiro-valor_uni*quantidade}")