# Escreva um programa que verifique se um número digitado pelo usuário é par ou ímpar.
# Saída de Dados (terminal):
# Digite um número: 7
# O número é ímpar.

num = int(input("Digite o número: "))
if num % 2 == 0:
    print(f'O Número {num} é par')
else:
    print(f'O Número {num} é impar')
    