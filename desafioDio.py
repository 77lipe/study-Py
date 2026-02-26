# Lê a linha de lançamentos do stdin
entrada = input("Digite a entrada, Despesas e receitas:").strip()

# Inicialize o saldo do dia
saldo = 0.0

# Divide os lançamentos pela vírgula
lancamentos = entrada.split(',')
print(lancamentos[0])

list_valor = []

for lancamento in lancamentos:
    tipo, valor = lancamento.strip().split()
    valor = float(valor)
    tipo = str(tipo)
    print("Tipo:", tipo, "Valor:",valor)

    list_valor.append(valor)
    # TODO: Atualize o saldo conforme o tipo de lançamento ('R' soma, 'D' subtrai)

# Imprima o saldo final com duas casas decimais
print(f"{saldo:.2f}")