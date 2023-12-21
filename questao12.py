# 12. Faça um programa que inicialize uma lista vazia, solicite ao usuário 10 números ímpares diferentes, 
# um por vez. Caso o número digitado seja par, solicite novamente um número, 
# até que o valor seja um número ímpar. 
# Depois disso, exiba os 10 números digitados.

listaImpar = []

for i in range(10):
    num = int(input("Digite o número impar: "))

    if num % 2 == 0:
        print("O número digitado não é ímpar. Digite novamente.")
        num = int(input("Digite um número ímpar: "))
    else:
        listaImpar.append(num)
print("Números ímpares digitados:", listaImpar)