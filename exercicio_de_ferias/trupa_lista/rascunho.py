valores = []
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

numeros_pares = []
numeros_impares = []
for valor in valores:
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

print("Números pares:", numeros_pares)
print("Números ímpares:", tuple(numeros_impares))
print("Quantidade de números pares:", len(numeros_pares))
print("Quantidade de números ímpares:", len(numeros_impares))
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
lista = []
for i in range(3):
    lista.append(input("Digite as letras: "))
print(lista)
for i, p in enumerate(lista):
    print(i+1,"-",p)
