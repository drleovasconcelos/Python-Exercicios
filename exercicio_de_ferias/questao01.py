# Exercício 01
# Faça um programa que receba dois números inteiros e exiba a soma deles.
# Saída de Dados (terminal):
# Digite o primeiro número: 5
# Digite o segundo número: 3
# A soma é: 8

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
x = (num1, num2)
y = sum(x)
print("A soma é: ", y)