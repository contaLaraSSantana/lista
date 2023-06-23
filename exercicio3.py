#Crie um programa onde o usuário posso digitar quantos números ele quiser.
#Depois mostre qual é a soma de todos os números e qual é o menor
num = []
while True:
    num.append(int(input('Digite um número: ')))
    res = str(input("Para continuar digite 1 e para sair digite 0: "))
    if res in "0":
        soma = sum(num)
        print(f'A soma dos números é igual a: {soma}')
        maior = max(num)
        menor = min(num)
        print(f'Maior: {maior}')
        print(f'Menor: {menor}')
        break