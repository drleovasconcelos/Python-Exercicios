# A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade06.py.
# Aproveite todo o algoritimo desenvolvido anteriormente e pergunte ao usuário se ele
# deseja recuperar a lista de compras apagada. Se sim, adicione os elementos excluídos
# novamente à lista principal (lembre-se: no exercício anterior, você os guardou na cópia
# da lista). Ainda, exiba a mensagem: "Sua lista de compras foi recuperada com
# sucesso!". Finalmente, limpe a cópia da lista e exiba a lista de compras recuperada.


# p1 - perguntar se deseja recuperar os item da lista de compras ok
# p2 - se sim, adicionar os elementos excluídos ok
# p3 - msg "Sua lista de compras foi recuperada com sucesso!"
# p5 - limpe a cópia da lista
# p6 - exiba a lista de compras recuperada.

# Criando uma lista de compras
lista_de_compras = ['arroz', 'feijão', 'macarrão']


opcao = input("Deseja eliminar os itens da lista de compras? Sim ou Não = ")
if opcao.lower() == "sim":
    copia_lista = lista_de_compras[:] #serve para copiar
    print ("Lista antiga é: ", copia_lista)
    lista_de_compras.clear()   ##limpa a lista
    print("Sua lista de compras tem 0 itens")
    opcao_visualizar = input("Deseja vizualizar a lista antiga? Sim ou Não = ")
    if opcao_visualizar.lower() == "sim":
        print("A lista antiga é: ", copia_lista)
    else:
        print("Não quero visualizar")

    opcao_recuperar = input("Deseja recuperar os itens da lista de compras? Sim ou Não = ")
    if opcao_recuperar.lower() == "sim":
        lista_de_compras.extend(copia_lista)
        print("Sua lista de compras foi recuperada com sucesso!")
        copia_lista.clear() 
        print("Lista de Compras: ", lista_de_compras)

else:
      print("Fim")