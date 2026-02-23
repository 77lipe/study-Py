nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
nota5 = float(input("Digite a quinta nota: "))

notas = [nota1, nota2, nota3, nota4, nota5]

media = sum(notas) / 5

if nota1 > nota2: 
    maior = nota1 
elif nota2 > nota3:
    maior = nota2
elif nota3 > nota4:
    maior = nota3
elif nota4 > nota5:
    maior = nota4
else:
    maior = nota5


notas_maior_media = []
count = 0
for i in notas:
    if i > 6:
        notas_maior_media.append(i)
        count += 1
        
print(f"\n\nMÉDIA GERAL: {media}\nMAIOR NOTA: {maior}\n{count} notas acima da Média!!")