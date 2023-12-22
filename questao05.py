# 05. Faça um programa que leia dois conjuntos de números inteiros, tendo
# cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
# conjuntos. interseção de dois grupos em python

a = (1, 2, 4, 5, 6, 7, 8, 9, 10)
b = (4, 5, 8, 12, 6, 7, 15, 13, 22, 10)
intersecao = []

for i in a:
    if i in b:
        intersecao.append(i)
        print("Interseção: ", intersecao)