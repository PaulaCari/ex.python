print('Ola Mundo!!!')
print("~~~~"*8)
# eto é um comentario claro e objetivo
'''
comentario de varia
linhas
'''

#ERROR control de resposta do codigo com essa importação
import warnings
warnings.filterwarnings('ignore')



#dados primitivos
#são numeros positivos e negativos e ozero

valor = 1
print(type(valor))

a = -99
b = 0
c = int('1000')
d = 10_000_000
print('tipo de dado de a: ')
print(type(a))
print(('tipo de dabo de  b: '))
print(type(b))
print(('tipo de dabo de  c: ',c))
print(type(c))
print(type(d))
print(d+c)
print("~~~~"*8)
print()


#DADOS COMPLEXOS
a = 30
b = 90 + 10j
c = a + b
print(a)
print(c)
print(type(c))
print(c.real)
print(c.imag)
print("~~~~"*8)


#PONTOS FLUTUANTES

a = 0
b = 0.0
c= .1
print(type(a))
print(type(b))
print(type(c))
print("~~~~"*8)

#BOLEANOS
a = True
b = False
print(type(a))
print(type(b))

k = True
l = False
m = bool(0) #False
n = bool(1) #True
o = bool(0.00000000001)
print('O valor de "k" é: ')
print(k)
print(type(k))
print('O tipo de "o" é: ')
print(o)
print(type(o))
print('O tipo de "m" é: ')
print(m)
print(type(m))
print("~~~~"*8)


#STRINGS SEQUENCIA DE CARATERES
a = 'Frase:'
b = 'este é uma frase'
c = ''' é este é  uma frase 
    miltilinha de tres linhas'''
d = 'meu gato se chama "mingau"'

print(a)
print(b)
print(c)
print(d)
print("~~~~"*8)


print('Digite seu nome: ')
x = input()
print('ola, '+x)


x= input("digite sua idade: ")
x = int(x)
x = str(x + 7)

print("sua idade é: " + x)
print("~~~~"*8)


a = 1
b = -99.9
c = 0

print(bin(173))
print(oct(42))
print(hex(404))
print(bin(17))
print(hex(0b10001))
print("~~~~"*8)


num = 'a' * 10
print(num)
num = 'a'*3 + 'i'*2
print(num)
print("~~~~"*8)


mult = 2
mult *= 3
print(mult)
print("~~~~"*8)


exp = 4
exp **= 2
print(exp)
print("~~~~"*8)

a = 2
b = 5
c = b + a
b += a
b = b + a
print(b)
print(c)
print("~~~~"*8)


teste_1 = True
teste_2 = not teste_1
print(teste_2)

teste_1 = not True
print(teste_1)
print("~~~~"*8)


var = 42
print(f' um numero curioso é: {var}')
print("~~~~"*8)


temp_fahrem = 150
print(f"A temperatur em graus celsus é:\ {round((temp_fahrem-32) * (5/9),2)} Celsus")
print("~~~~"*8)


print("pai" , "mae" ,"filha" ,sep='\n')
print("~~~~"*8)


num = '0123456789'
num_com_metodo = ',' .join(num)
print(num_com_metodo)
print("~~~~"*8)


num_separados = num_com_metodo.split(',')
print(num_separados)
print(type(num_separados))
print("~~~~"*8)


a = 5
b = 2
if a > b:
    print(f'{a} é maior que {b}')
print('O programa terminou')
print("~~~~"*8)

a = 512
if a > 1000:
    print(f'{a} é maior que 1000')
elif a > 100:
    print(f'{a} é maior que 100')
elif a > 10:
    print(f'{a} é maior que 10')
elif a == 10:
    print(f'{a} é igual a 10')
else:
    print(f'{a} é menor que 10')
print("~~~~"*8)


maquina_ligada = True
acesso_bloqueado = False
if maquina_ligada:
    acesso_bloqueado=True
print(acesso_bloqueado)

maquina_ligada = True
acesso_bloqueado = False
if not maquina_ligada:
    acesso_bloqueado=False
print(acesso_bloqueado)

maquina_ligada = True
acesso_bloqueado = False
processo_em_execução = False
if maquina_ligada and acesso_bloqueado:
    processo_em_execução=True
print("~~~~"*8)



temperatura = 98
while temperatura <= 100:
    print(temperatura)
    temperatura += 1  # temperatura = temperatura +1
print("~~~~"*8)


for vezes in range(1):
    print(f'Este loop sera repetido {vezes} vezes')
print("~~~~"*8)


for num in range(5, 11):
    print(f'o loop é de {num} repetiçoes')
print("~~~~" * 8)
print()


for num in range(5, 11, 2):
    print(f'o loop é de {num} repetiçoes')
print("~~~~"*8)

for valor in range(4):
    if valor % 2 == 0:
        print(f'O numero é {valor} é par')
    else:
        print(f'O numero é {valor} e impar')
print("~~~~" * 8)


lista = ['abacaxi', 'amora', 'maça', 'uva', 'melancia']
for frutas in lista:
    print(frutas)
print("~~~~"*8)


temperatura = 101
if temperatura >= 100:
    print('Deligar aquecedor')
print("~~~~"*8)
print()

temperatura = 99
if temperatura >= 100:
    print('Deligar aquecedor')
else:
    print('Manter aquecedor ligado')
print("~~~~"*8)


temperatura = 49
if temperatura >= 100:
    print('Desligar aquecedor')
elif temperatura <= 50:
    print('Manter aquecedor ligado')
    print('Ligar o segundo aquecedor')
print("~~~~" * 8)


aqueceddor_danificado = True
temperatura = 45

if temperatura <= 50 and not aqueceddor_danificado:
    print('Manter aquecedor ligado')
    print('Ligar o segundo aquecedor')
elif temperatura > 100:
    print('desligar aqucedor')
elif aqueceddor_danificado:
    print('reparar quecedor')
else:
    print('Nao precissa fazer nada')
print("~~~~"*8)

names = ['jimmy', 'rose', 'max', 'nina', 'philip']
for name in names:
    if len(name) != 4:
        continue
    print(f' hello {name}')
    if name == 'nina':
        break
print('Done')
print("~~~~"*8)

compra = ['laranja', 'abacaxi', 'mamao']
compra.insert(1, 'morango')
print(compra)
print("~~~~"*8)

nome = str(input("digite seu nome: "))
print(len(nome))
print("~~~~"*8)

lista_compras = [' laranja',
                 'abacaxi',
                 'mamão']
print(len(lista_compras))
print("~~~~"*8)
print()




#1 Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

num_lista = []
for i in range(5):
    num = int(input('Digite o numero: '))
    num_lista.append(num)
print(num_lista)
print("~~~~"*8)
print()


#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
num_lista = []
for i in range(10):
    num = float(input('Digite o numero: '))
    num_lista.append(num)
print(num_lista)

num_lista.sort(reverse=True)
for i in num_lista:
    print(i)
print("~~~~"*8)
print()


#3 Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
media = 0
for i in range(4):
    notas.append(float(input('Nota '+ str(i+1) + ':')))
    media += notas[i]
media = media/4
print(notas)
print(media)
print("~~~~"*8)



#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes.

carateres_lista = []
consonantes= 0
for i in range(3):
    carateres_lista.append(input('carateres '+ str (i+1) + ':'))
    carater = carateres_lista[i]
    if(carater not in ('a', 'e','i', 'o', 'u')):
        consonantes += 1
print(consonantes)
print("~~~~"*8)



#5 Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
#números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

par = []
impar = []
listaNum = []
num = 0

for i in range(3):
    num = int(input("Digite um numero inteiro: "))
    listaNum.append(i)
if num % 2 == 0:
	print(par.append(num))
else:
    print(impar.append(num))

print(listaNum)
print(par)
print(impar)
print("~~~~"*8)



def imprime_lista(arg_lista):
    for elemento in arg_lista:
        print(elemento)
lista = list ('01234567')
imprime_lista(lista)
print("~~~~"*8)




