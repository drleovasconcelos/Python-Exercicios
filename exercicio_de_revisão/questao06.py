# 06. Faça um programa que armazene 50 números inteiros. 
# O programa deve gerar e imprimir uma segunda lista em que cada elemento é o 
# quadrado do elemento do primeiro.

import math 

lista = []
for i in range(5):
    numero = int(input("Adicione o número: "))
    lista.append(numero)
print(f'Lista: {lista}')
for n in lista:
    quadrado = int(math.sqrt(n))
    print(f"Número: {n}, Quadrado: {quadrado}")