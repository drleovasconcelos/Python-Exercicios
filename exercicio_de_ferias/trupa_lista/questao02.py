# A partir do arquivo criado na atividade anterior, crie um arquivo Python exercicio02.py.
# Após, exiba na tela (terminal) a lista de compras definida anteriormente. Na sequência,
# pergunte ao usuário se ele deseja remover algum item da lista. Se sim, pergunte ao
# usuário qual item ele desejar retirar, e repida o processo até que ele digite a palavra
# "fim". Ao final, exiba a lista com os itens retirados. Dica: utilize a função .remove().

lista = []
compras = int(input("Deseja cadastrar um item? 1 - Sim ou 2 - Não = "))
while compras == 1:
    item = input("Adicionar itens: ")
    lista.append(item)
    print("A Lista é: ", lista)
    compras = int(input("Deseja cadastrar um item? 1 - Sim ou 2 - Não = "))
else:
    remover = int(input("Deseja remover algum item: 1 - Sim ou 2 - Não = "))
    if remover == 1:
        item_remover = input("Qual item deseja remover: ")
        lista.remove(item_remover)
        print("A Lista é: ", lista)
        remover = int(input("Deseja remover algum item: 1 - Sim ou 2 - Não = "))
    else: 
        print("Fim")