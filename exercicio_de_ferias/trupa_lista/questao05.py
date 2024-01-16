# A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade06.py.
# Após, pergunte ao usuário se ele deseja apagar os itens da lista de compras. Se sim,
# antes de apagar os itens, crie uma cópia da lista de compras. Na sequência, exiba a lista
# de compras (com todos os itens) e conforme com o usuário se ele deseja excluir a lista.
# Caso afirmativo, exclua toda a lista e mostre a mensagem: "Sua lista de compras tem
# 0 itens". Em seguida, pergunte ao usuário se ele deseja vizualizar a lista antiga e, se
# verdade, exiba ao usuário a cópia da lista de compras conforme o exemplo abaixo.

# p1 - perguntar se deseja eliminar os item da lista de compras ok
# p2 - se sim, criar um cópia da lista e exibir ok
# p3 - excluir todos os itens da lista
# p4 - msg "Sua lista de compras tem 0 itens"
# p5 - deseja visualizar a lista antiga
# p6 - exibir a cópia da lista antiga

# Criando uma lista de compras
lista_de_compras = ['arroz', 'feijão', 'macarrão']


opcao = input("Deseja eliminar os itens da lista de compras? Sim ou Não = ")
while opcao.lower() == "sim":
        copia_lista = lista_de_compras[:] #serve para copiar
        print ("Lista antiga é: ", copia_lista)
        lista_de_compras.clear()   ##limpa a lista
        print("Sua lista de compras tem 0 itens")
        opcao_visualizar = input("Deseja vizualizar a lista antiga? Sim ou Não = ")
        if opcao_visualizar.lower() == "sim":
             print("A lista antiga é: ", copia_lista)
        else:
             print("Não quero visualizar")
else:
    terminar = input("Fim")