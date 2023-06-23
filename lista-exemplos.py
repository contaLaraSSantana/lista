fruta = ['Maçã','Banana','Abacaxi','Uva']
#estrutura da lista

#fruta = [] #lista vazia que posso adicionar elementos
#fruta = list() #lista vazia em função

# diferença entre tupla e lista é que ela é mutavel ja a tupla não
# além disso as tuplad não podem ficar vazias
# ()- tupla []-lista

fruta[3] = 'Melancia' #substitui elementos
print(fruta)

fruta.append('Laranja') #acrescenta algo no fim da lista
print(fruta)

fruta.insert(0,'Morango') #acrescenta na posição que eu escolher
print(fruta)

fruta.insert(1,'Uva')
print(fruta)

#fatiamento

#del pode apagar tudo
#formas de apagar por posição
del fruta [3]
print(fruta) #apagou a banana
#fruta.pop (3)
#fruta.remove("Abacaxi") # se tiver dois abacaxi ele apaga o primeiro

fruta.pop()# apaga o ultimo elemento
print(fruta)

#verificar se tem a fruta

#for c in fruta:
#    if c == "Abacaxi":
#        fruta.remove('Abacaxi')
#   else:
#       print ('Não encontrado')

#forma mais simples

if 'Morango' in fruta:
    fruta.remove('Abacaxi')
else:
    print('Não encontrado')
print(fruta)

#outra forma
if 'Morango' not in fruta:
    print('Não encontrado')
else:
    fruta.remove('Morango')
print(fruta)

#---------------------------------------------

#num = list(range(1 , 7)) #lista até o 6
#print(num)

num = [7,4,2,5,3,6]
num.sort() #ordem numérica
print(num)

num.sort(reverse = True) #ordem reversa
print(num)

#soma
soma = sum(num)
print(f'Soma: {soma}')

#ver qual o maior e o menor
maior = max (num)
menor = min(num)
print(f'Maior: {maior}')
print(f'Menor: {menor}')
#
maiores = max(fruta,key =len)
menores = min (fruta, key=len)
print(f'Maior: {maiores}')
print(f'Menor:{menores}')
####
num2=num[:] #faz uma cópia de num1 e armazena num2 as tornando independentes
num2[1]=9
print(f'lista:{num}')
print(f'lista:{num2}')

####
num1 = []
while True:
    num1.append(int(input('Digite um número: ')))
    res = str(input("Deseja continuar [s/n]"))
    if res in "n":
        break
    print(f'Os números são {num1}')
