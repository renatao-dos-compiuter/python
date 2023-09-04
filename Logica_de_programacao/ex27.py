#ex6: Implementar um programa que retorne um texto que represente a forma de uma linha a partir do tamanho de pontos que a compõem

n=int(input("Dgite um número: "))
contador=1

while contador<=n:
    print("*", end= ' ')
    contador=contador+1