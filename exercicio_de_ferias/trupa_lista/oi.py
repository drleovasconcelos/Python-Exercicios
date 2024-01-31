lista = []
# Usando o Input() vamos coletar do usuário qual o número a ser adicionado.
for i in range(15):
    numero = int(input('Informe o número: '))
    lista.append(numero)
    
for i,l in enumerate(lista):
    
    print(i+1, " -> ", l)
    