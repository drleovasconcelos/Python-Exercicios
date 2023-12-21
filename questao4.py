# Faça um programa que imprima a porcentagem dos alunos que gasta acima de
# R$200,00 com outras despesas. O número de alunos com renda pessoal maior
# que a renda familiar e a porcentagem gasta com alimentação e outras despesas
# em relação às rendas pessoal e familiar.


qdeAlunosTotal = int(input("Quantos alunos em sala: "))
alunos_acima_200 = 0
alunos_renda_pessoal_maior = 0
total_gastos_alimentacao = 0
total_gastos_outras_despesas = 0

for i in range(1, qdeAlunosTotal+1): #iniciamos em 1 -> caminha até 9 + 1 = 10
    print(f"\nInformações para o aluno {i}:")
    rendaPessoal = float(input("Digite a sua Renda pessoal: "))
    rendaFamiliar = float(input("Digite a sua Renda Familia: "))
    gastoAlimentação = float(input("Total gasto com alimentação: "))
    gastoOutrasDespesas = float(input("Total gasto com outras despesas: "));
    if rendaPessoal > rendaFamiliar: #renda pessoal maior que renda familiar
        alunos_renda_pessoal_maior = alunos_renda_pessoal_maior + 1
    
    total_gastos_alimentacao += gastoAlimentação
    total_gastos_outras_despesas += gastoOutrasDespesas

    if gastoOutrasDespesas > 200:
        alunos_acima_200 = alunos_acima_200 + 1
    
#porcetagem
porcentagem_acima_200 = (alunos_acima_200 / qdeAlunosTotal) * 100
porcentagem_renda_pessoal_maior = (alunos_renda_pessoal_maior / qdeAlunosTotal) * 100
porcentagem_gastos_alimentacao = (total_gastos_alimentacao / total_gastos_outras_despesas) * 100
porcentagem_gastos_outras_despesas = (total_gastos_outras_despesas / total_gastos_alimentacao) * 100

print(f"\nPorcentagem de alunos que gastam acima de R$200,00 com outras despesas: {porcentagem_acima_200}%")
print(f"Número de alunos com renda pessoal maior que a renda familiar: {alunos_renda_pessoal_maior}")
print(f"Porcentagem gasta com alimentação em relação às despesas totais: {porcentagem_gastos_alimentacao}%")
print(f"Porcentagem gasta com outras despesas em relação às despesas totais: {porcentagem_gastos_outras_despesas}%")