soma=0
media_maior7=0
lista=[]

for contador in range (1,5):
    for i in range (1,11):
        nota=int(input(f"Digite a {i}° nota do {contador} aluno (0-10): "))
        soma+=nota
    media=soma/10
    lista.append(media)
    if media >=7:
        media_maior7+=1
    media=0
    soma=0
print(lista)
print(f"O número de alunos que tirou uma nota maior ou igual a 7 é {media_maior7}")