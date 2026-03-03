# Lê a linha de lançamentos do stdin
entrada = input("Digite a entrada, Despesas e receitas:").strip()

# Inicialize o saldo do dia
saldo = 0.0

# Divide os lançamentos pela vírgula
lancamentos = entrada.split(',')
print(lancamentos[0])

R = []
D = []

for lancamento in lancamentos:
    tipo, valor = lancamento.strip().split()
    valor = float(valor)
    tipo = str(tipo)
    #print("Tipo:", tipo, "Valor:",valor)
    if tipo == "R":
        R.append(valor)
    else:
        D.append(valor)
    # TODO: Atualize o saldo conforme o tipo de lançamento ('R' soma, 'D' subtrai)



valor_receita = sum(R)
valor_despesas = sum(D)

saldo = valor_receita - valor_despesas

#print("lista R:", R)
#print("lista D:", D)

# Imprima o saldo final com duas casas decimais
print(f"{saldo:.2f}")