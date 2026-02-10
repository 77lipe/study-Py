import json

nome = input(str("Qual seu nome?"))
idade = input(str("Qual as sua idade?"))

estados_brasil = ["SP", "RJ", "MT", "TS"]
print(f'Ex: {estados_brasil}')
estado = input(str("Em qual Estado do Brasil você reside?"))
#print(estado)

estados_nome_json = ''' 
    { 
    "estado1": {
        "estado": "São Paulo",
        "gentilico": "Paulista"
    },
    "estado2": {
        "estado": "Rio de Janeiro",
        "gentilico": "Carioca"
    }
}
'''
dados_estados_json = json.loads(estados_nome_json)

if estado == estados_brasil[0]:
    print(f'Olá {nome}, você possui {idade} anos!\nE mora em {dados_estados_json["estado1"]["estado"]}({dados_estados_json["estado1"]["gentilico"]})')
elif estado == estados_brasil[1]:
    print(f'Olá {nome}, você possui {idade} anos!\nE mora em {dados_estados_json["estado2"]["estado"]}({dados_estados_json["estado2"]["gentilico"]})')
elif estado == estados_brasil[2]:
    print(f'Olá {nome}, você possui {idade} anos!\nE mora em {estados_brasil[2]}')
elif estado == estados_brasil[3]:
    print(f'Olá {nome}, você possui {idade} anos!\nE mora em {estados_brasil[3]}, você é ')



