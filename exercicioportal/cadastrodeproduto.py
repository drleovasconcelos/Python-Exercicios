# RIAR UM SISTEMA COM AS SEGUINTES OPÇÕES

# Adicionar produtos: O usuário pode adicionar um novo produto à lista informando o nome, a quantidade e o valor unitário do produto. 
# O programa calcula automaticamente o valor total do produto (quantidade * valor unitário) e atualiza o valor total de todos os 
# produtos.# Ver a lista de produtos: O programa exibe a lista de produtos adicionados até o momento, mostrando o nome do produto, 
# o valor unitário, a quantidade e o valor total do produto. Além disso, exibe o valor total de todos os produtos da lista.
# Atualizar produtos: O usuário pode atualizar as informações de um produto existente na lista. O programa solicita o nome do 
# produto que deseja atualizar e, em seguida, permite editar o nome, a quantidade e o valor unitário do produto. O programa recalcula
# automaticamente o valor total do produto e o valor total de todos os produtos.# Remover produto: O usuário pode remover um produto 
# da lista informando o nome do produto que deseja remover. O programa atualiza automaticamente o valor total de todos os produtos.
# Encerrar programa: Encerra a execução do programa.
# O programa utiliza uma lista para armazenar os produtos, onde cada produto é representado por um dicionário com as informações: 
# "produto", "valor", "quantidade" e "total". A variável totalProdutos é utilizada para armazenar o valor total de todos os produtos 
# da lista.


def adicionar_produto(lista_produtos, total_produtos):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))
    
    total = quantidade * valor_unitario
    produto = {"produto": nome, "quantidade": quantidade, "valor": valor_unitario, "total": total}
    
    lista_produtos.append(produto)
    total_produtos += total
    
    print("Produto adicionado com sucesso!")
    return total_produtos

def ver_lista_produtos(lista_produtos, total_produtos):
    print("Lista de Produtos:")
    for produto in lista_produtos:
        print(f"Produto: {produto['produto']} | Quantidade: {produto['quantidade']} | Valor Unitário: R${produto['valor']} | Total: R${produto['total']}")
    print(f"Valor Total de todos os Produtos: R${total_produtos}")

def atualizar_produto(lista_produtos, total_produtos):
    nome_produto = input("Digite o nome do produto que deseja atualizar: ")
    
    for produto in lista_produtos:
        if produto["produto"] == nome_produto:
            produto["produto"] = input("Digite o novo nome do produto: ")
            produto["quantidade"] = int(input("Digite a nova quantidade do produto: "))
            produto["valor"] = float(input("Digite o novo valor unitário do produto: "))
            produto["total"] = produto["quantidade"] * produto["valor"]
            
            print("Produto atualizado com sucesso!")
            return
        
    print("Produto não encontrado na lista.")

def remover_produto(lista_produtos, total_produtos):
    nome_produto = input("Digite o nome do produto que deseja remover: ")
    
    for produto in lista_produtos:
        if produto["produto"] == nome_produto:
            total_produtos -= produto["total"]
            lista_produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
        
    print("Produto não encontrado na lista.")

def main():
    lista_produtos = []
    total_produtos = 0
    
    while True:
        print("\n1 - Adicionar Produto")
        print("2 - Ver Lista de Produtos")
        print("3 - Atualizar Produto")
        print("4 - Remover Produto")
        print("5 - Encerrar Programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            total_produtos = adicionar_produto(lista_produtos, total_produtos)
        elif opcao == "2":
            ver_lista_produtos(lista_produtos, total_produtos)
        elif opcao == "3":
            atualizar_produto(lista_produtos, total_produtos)
        elif opcao == "4":
            remover_produto(lista_produtos, total_produtos)
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
