#Crie um programa onde o usuário possa digitar vários valores numéricos e
#cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = []
while True:
    num.append(int(input('Digite um número: ')))
    res = int(input("Para continuar digite 1 e para sair digite 0: "))
    if res in num:
        num.pop()
        break
    num.sort
    print(num)