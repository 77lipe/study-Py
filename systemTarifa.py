vagas = [1,2,3,4,5]
reservado = []

print("Vagas disponíveis:", vagas)
lugar = int(input("Digite o número da vaga estacionado: "))

for v in vagas:
    if v == lugar:
        print(f"Lugar reservado: {v}")
        vagas.remove(v)
        reservado.append(v)
        break

print(" ")
print("Vagas disponíveis:", vagas)
print("Vagas reservadas:", reservado)


tempo_estacionado = float(input(f"Tempo do Carro estacionado na vaga {reservado}, em horas: "))

def aplicar_taxa(tempo_estacionado, taxa=30,tarifa=0.05):
    tarifa = tempo_estacionado * tarifa
    valor_final = taxa + tarifa * 100

    return valor_final

val_final = aplicar_taxa(tempo_estacionado)

print("\nDébito a ser pago:", val_final)

pagamento = float(input("Coloque o valor do pagamento: "))
def verificar_pagamento(pay):
    if pay < val_final:
        return "Saldo inválido!!"
    else:
        return "Pagamento realizado!!"

print(verificar_pagamento(pagamento))

for r in reservado:
    reservado.remove(r)
    vagas.append(r)
    break

print("Vagas reservada:", reservado)
print("Vagas Disponíveis:", vagas)



## pop() -> deleta valor de uma lista, pega por posição
## remove() -> remove um valor específico 