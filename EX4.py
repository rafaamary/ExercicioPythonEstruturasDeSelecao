'''Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o 
resultado da operação solicitada.'''

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
operacao = str(input('Qual opercao voce deseja realizar? '))

if (operacao == '+'):
    res = n1+n2
elif (operacao == '-'):
    res = n1 - n2
elif (operacao == '*'):
    res = n1 * n2
elif (operacao == '/'):
    res = n1 / n2

print('O resultado da operacao e: ', res)