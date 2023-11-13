# Implementar uma função para calcular o salário líquido de um funcionário, a partir de seu salário base,
# do bônus mensal (em %) e do total de descontos.
def salario_com_bonus (x):
    porcentagem=x*(bonus/100)
    return porcentagem


salario_com_bonus=salario_com_bonus(int(input("Salário: ")))
bonus=int(input("Bônus: "))