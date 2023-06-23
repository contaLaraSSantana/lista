#Crie um programa onde o usuário posso digitar cinco valores numéricos
#e cadastre-os em uma lista. No Final mostre a lista ordenada.
num= []
for i in range (5):
    num.append(int(input('Digite um número: ')))
num.sort()
print(num)