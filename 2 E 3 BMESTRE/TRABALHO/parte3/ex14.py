print("As opções são:")

print("1. Candidata Juliana ")
print("2. Candidato Marcos ")
print("3. Candidato João ")
print("4. Nulo ")
print("5. Branco ")

juliana=0
marcos=0
joao=0
nulo=0
branco=0
voto= int(input("Entre com o seu voto: "))
while voto!=6:
    voto= int(input("Entre com o seu voto: "))
    if voto ==1:
        juliana+=1
    elif voto==2:
        marcos+=1
    elif voto==3:
        joao+=1
    elif voto==4:
        nulo+=1
    elif voto==5:
        branco+=1
    else:
        print("Opção inválida!")
soma=juliana+marcos+joao+branco+nulo

print(f"A candidata Juliana recebeu {juliana} votos.")
print(f"O candidata Marcos recebeu {marcos} votos.")
print(f"O candidato João recebeu {joao} votos.")
print(f"{(nulo/soma)*100:.2f}%.")
print(f"{(branco/soma)*100:.2f}%.")

if joao>juliana and joao> marcos:
    print("O vencedor das eleições é o candidato João!")
if juliana>joao and juliana> marcos:
    print("O vencedor das eleições é a candidata Juliana!")
if marcos>joao and marcos> juliana:
    print("O vencedor das eleições é o candidato Marcos!")