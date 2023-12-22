qtdevolume = pesoTotal = 0
resp = int(input("Deseja cadastrar uma caixa? 1 - Sim ou 2 - Não"))
while resp == 1:
    qtdevolume < 200
    qtdevolume+=1 #qtdevolume = qtdevolume + 1
    peso = float(input("informe o peso da Caixa: "))
    pesoTotal+=peso # pesoTotal = pesoTotal + peso
    pesoTotal < 10000
    resp = int(input("Deseja cadastrar mais uma caixa? 1 - Sim ou 2 - Não \n"))
else:
    print("Programa encerrado")    

print("Quantidade de Volumes: ", qtdevolume)
print("Peso total dos Volumes: ", pesoTotal)
mediaVolume = pesoTotal / qtdevolume
print("Peso médio dos Volumes: ", mediaVolume)