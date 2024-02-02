lista = []
for i in range(3):
    lista.append(input("Digite as letras: "))
print(lista)
for i, p in enumerate(lista):
    print(i+1,"-",p)
