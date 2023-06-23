#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

num = []
while True:
    num.append(int(input('Digite um número: ')))
    res = str(input("Para continuar digite 1 e para sair digite 0: "))
    if res in "0":
        print("Foram digitados: ", len(num)," números")
        num.sort(reverse=True)
        print("Ordenada de forma decrescente: ", num)
        break
    if 5 in num :
        print('O 5 foi digitado')
    else:
        print('O número 5 não foi digitado')