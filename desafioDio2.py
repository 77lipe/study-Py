entrada = input().strip()

transferencias = entrada.split(' ')

valores_rep = {}
transacoes_unicas = []

for i in transferencias:
    if i in valores_rep:
        valores_rep[i].append(i)
    else:
        valores_rep[i] = [i]
        

for item in valores_rep:
    transacoes_unicas.append(item)

print(*transacoes_unicas)

## "*" antes de uma lista no print, remove o [] e as vírgulas entre os valores