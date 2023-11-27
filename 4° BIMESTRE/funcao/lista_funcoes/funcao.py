def dobro(x):
    resultado=x*2
    return resultado

x=int(input("Infrome um número: "))
print(f"O dobro é: {dobro(x)}")

# O "def" cria a função, depois damos nome a essa função. Depois, entre parênteses, damos o parâmetro. Logo após, definimos o que a função vai fazer. O "return" se trata de un comando que explicita o que vai ser retornado.

def quadrado(x):
    quadrado=x**2
    return quadrado

numero=int(input("Informe um número: "))
print(f"O quadrado é: {quadrado(numero)}")