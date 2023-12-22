# Crie um programa que verifique se um número digitado pelo usuário é primo ou não com o WHILE.
def verificar_primo(numero):
    if numero < 2:
        return False
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True

# Solicitar input do usuário
numero_digitado = int(input("Digite um número inteiro positivo: "))

# Verificar se o número é primo e exibir o resultado
if verificar_primo(numero_digitado):
    print(f"{numero_digitado} é um número primo.")
else:
    print(f"{numero_digitado} não é um número primo.")
