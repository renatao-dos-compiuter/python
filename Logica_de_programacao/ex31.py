# ex10: Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber 
# um número desconhecido de valores referentes aos preços das mercadorias. O valor zero deve ser informado
# pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar
# o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta
#operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

print("Mercearia")
contador=1
valor=float(input("Produto 1: R$"))
soma=0

while valor!=0:
    contador=contador+1
    soma=soma+valor
    valor=float(input("Produto 1: R$"))
print(f"Total: R${soma}")