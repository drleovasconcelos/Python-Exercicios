# [PY-A07] Você foi contratado(a) para desenvolver um programa que gerencie um dicionário de alunos onde a chave deste dicionário é o número de matrícula dos próprios alunos. O programa deve permitir adicionar, remover, atualizar e listar os alunos.
# Para isso, você deve implementar um módulo que contém as seguintes funções:
# AdicionarAluno(): Solicita ao usuário que digite o nome e o número de matrícula de um aluno e adicione-o ao dicionário de alunos.
# RemoverAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e remove-o do dicionário de alunos.
# AtualizarAluno(): Solicita ao usuário que digite o número de matrícula de um aluno e atualize o nome desse aluno no dicionário .
# VerAlunos(): Lista todos os alunos cadastrados, exibindo o número de matrícula e o nome de cada um.
# Lembre Se de Modularizar o código

def adicionar_aluno(dic_alunos):
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")
    dic_alunos[matricula] = nome
    print("Aluno adicionado com sucesso!")

def remover_aluno(dic_alunos):
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")
    if matricula in dic_alunos:
        del dic_alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def atualizar_aluno(dic_alunos):
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")
    if matricula in dic_alunos:
        novo_nome = input("Digite o novo nome do aluno: ")
        dic_alunos[matricula] = novo_nome
        print("Nome do aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")

def ver_alunos(dic_alunos):
    if dic_alunos:
        print("Lista de Alunos:")
        for matricula, nome in dic_alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
    else:
        print("Nenhum aluno cadastrado.")

def main():
    alunos = {}

    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno(alunos)
        elif opcao == "2":
            remover_aluno(alunos)
        elif opcao == "3":
            atualizar_aluno(alunos)
        elif opcao == "4":
            ver_alunos(alunos)
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
