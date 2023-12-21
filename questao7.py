# 07. Crie um programa para ler um conjunto de 100 números reais e informe:
# • quantos números lidos são iguais a 30
# • quantos são maior que a média
# • quantos são iguais a média

lista = []

for i in range(10):
    numeros = float(input("Digite o numero real: "))
    lista.append(numeros)

media = sum(numeros) / len(numeros)

iguais_a_30 = 0
maiores_que_media = 0
iguais_a_media = 0

for i in lista:
    if i == 30:
        iguais_a_30 += 1
    if i > media:
        maiores_que_media += 1
    if i == media:
        iguais_a_media += 1

print(f"Quantidade de números iguais a 30: {iguais_a_30}")
print(f"Quantidade de números maiores que a média: {maiores_que_media}")
print(f"Quantidade de números iguais à média: {iguais_a_media}")