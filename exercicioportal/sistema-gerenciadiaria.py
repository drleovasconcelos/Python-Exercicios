tarefa = {
    'nome': 'Estudar Python',
    'descricao': 'Estudar Python para melhorar minhas habilidades de programação.',
    'prioridade': 'Alta',
    'categoria': 'Estudo',
    'concluida': False
}
def adicionar_tarefa(lista_tarefas, tarefa):
    lista_tarefas.append(tarefa)

def listar_tarefas(lista_tarefas):
    for idx, tarefa in enumerate(lista_tarefas, start=1):
        print(f"Tarefa {idx}: {tarefa['nome']} - {tarefa['descricao']}")

def marcar_como_concluida(lista_tarefas, idx_tarefa):
    lista_tarefas[idx_tarefa]['concluida'] = True

def exibir_tarefas_por_prioridade(lista_tarefas):
    prioridades = {}
    for tarefa in lista_tarefas:
        prioridade = tarefa.get('prioridade', 'N/A')
        if prioridade not in prioridades:
            prioridades[prioridade] = []
        prioridades[prioridade].append(tarefa)
    
    print("Tarefas por Prioridade:")
    for prioridade, tarefas in sorted(prioridades.items()):
        print(f"Prioridade: {prioridade}")
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f"Tarefa {idx}: {tarefa['nome']} - {tarefa['descricao']}")

def exibir_tarefas_por_categoria(lista_tarefas):
    categorias = {}
    for tarefa in lista_tarefas:
        categoria = tarefa.get('categoria', 'N/A')
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(tarefa)
    
    print("Tarefas por Categoria:")
    for categoria, tarefas in categorias.items():
        print(f"{categoria}:")
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f"Tarefa {idx}: {tarefa['nome']} - {tarefa['descricao']}")

def menu():
    lista_tarefas = []
    
    while True:
        print("\n==== MENU ====")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome da Tarefa: ")
            descricao = input("Descrição da Tarefa: ")
            prioridade = input("Prioridade da Tarefa: ")
            categoria = input("Categoria da Tarefa: ")
            tarefa = {'nome': nome, 'descricao': descricao, 'prioridade': prioridade, 'categoria': categoria, 'concluida': False}
            adicionar_tarefa(lista_tarefas, tarefa)
            print("Tarefa adicionada com sucesso!")
        elif opcao == "2":
            listar_tarefas(lista_tarefas)
        elif opcao == "3":
            idx_tarefa = int(input("Índice da Tarefa a ser marcada como concluída: ")) - 1
            marcar_como_concluida(lista_tarefas, idx_tarefa)
            print("Tarefa marcada como concluída!")
        elif opcao == "4":
            exibir_tarefas_por_prioridade(lista_tarefas)
        elif opcao == "5":
            exibir_tarefas_por_categoria(lista_tarefas)
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
