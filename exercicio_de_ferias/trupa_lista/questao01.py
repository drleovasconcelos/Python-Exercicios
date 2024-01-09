# Crie um arquivo Python exercicio01.py. Após, defina uma variável do tipo lista (list)
# vazia. Na sequência, implemente um programa para perguntar ao usuário se ele deseja
# adicionar itens à lista de compras. Se sim, o usuário deve adicionar itens à lista
# enquanto (while) não for digitada a palavra "FIM". Ao final, a lista de compras com os
# itens adicionados pelo usuário. Dica: utilize a função .append().

lista_de_compra = []
compras = int(input("Deseja cadastrar um item? 1 - Sim ou 2 - Não = "))
while compras == 1:
    item = input("Adicionar itens: ")
    lista_de_compra.append(item)
    print("A Lista é: ", lista_de_compra)
    compras = int(input("Deseja cadastrar um item? 1 - Sim ou 2 - Não = "))
else:
    terminar = input("Fim")
