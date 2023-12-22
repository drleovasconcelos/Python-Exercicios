# Faça um programa que verifique se um número digitado pelo usuário é positivo, negativo
# ou zero. Dica: utilize condicionais (if...elif...else) ou três blocos ifs distintos.
# Saída de Dados (terminal):
# Digite um número: -2.5
# O número é negativo.

num = float(input("Digite o número: "))
if num == 0:
    print("Número é zero")
elif num > 0:
    print("Número é positivo")
else: 
    print("Número é negativo")