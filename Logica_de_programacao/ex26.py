#ex5: Implementar uma função que escreva no terminal o dobro dos números naturais de 1 até um número informado. A mensagem deve estar no formato: "O dobro de X é Y".

n=int(input("Digite um número inteiro: "))
contador=1
contador2=2

while contador<=n:
    print(f"O dobro de {contador} é {contador2*contador} ")
    contador=contador+1