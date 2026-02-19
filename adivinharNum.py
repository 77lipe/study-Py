import random

numero = random.randint(1,100)
#print(numero)

tentativa = int(input("Tente adivinhar o número entre 1 - 100: "))
cont = 1

def acertou(tentativa):
   if tentativa == numero:
        return True
   
if acertou(tentativa) != True:
    while tentativa != numero:
        if tentativa < numero:
            print(f"\nTente um número maior que {tentativa}")
            cont += 1
            tentativa = int(input("Nova tentativa: "))
        else:
            print(f"\nTente um número menor que {tentativa}")
            cont += 1
            tentativa = int(input("Nova tentativa: "))
    if tentativa == numero:
        print(f'\nVocê acertou o número!!\n"{numero}"')
else:
    print(f'\nVocê acertou o número!!\n"{numero}"')

print(f"Você realizou {cont} tentativas!!")