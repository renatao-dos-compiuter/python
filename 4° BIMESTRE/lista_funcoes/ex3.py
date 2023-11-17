def valor_parcela(x):
    valor_parcela=valor/quant_parcela
    return valor_parcela

valor=float(input("Qual o valor total da compra? "))
quant_parcela=int(input("Vai dividir em quantas vezes? "))

print(f"Sua compra de R${valor} em {quant_parcela}x de R$ {valor_parcela(valor_parcela)} foi concluída!")