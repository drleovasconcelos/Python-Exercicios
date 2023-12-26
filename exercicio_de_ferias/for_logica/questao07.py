# Crie um programa que verifique se um aluno foi aprovado ou reprovado em uma
# disciplina, considerando que a média para aprovação é 7.0.
# Saída de Dados (terminal):
# Digite a primeira nota: 6.5
# Digite a segunda nota: 8.0
# Aluno aprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")