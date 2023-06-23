#Escreva um programa que solicite vários números ao usuário, sendo um de cada
#vez, possibilitando encerrar a entrada de dados informando zero. Adicione os números
#informados em uma lista e, ao final do programa, imprima a soma de todos os números,
#a multiplicação de todos os números, o maior e o menor número informado.

num1 = []
multiplica = 1

while True:
    num1.append(int(input('Digite um número: ')))
    res = str(input("Para continuar digite 1 e para sair digite 0: "))
    if res in "0":
        print(f'Os números são {num1}')
        soma = sum(num1)
        print(f'A soma dos números é igual a: {soma}')
        maior = max(num1)
        menor = min(num1)
        print(f'Maior: {maior}')
        print(f'Menor: {menor}')
        print(f'Multiplicação: {multiplica}')
        break

    print(f'Os números são {num1}')

    for i in num1:
        multiplica *= i
        print(f'Multiplicação: {multiplica}')


