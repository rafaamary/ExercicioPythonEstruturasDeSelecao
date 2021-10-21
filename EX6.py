'''Um ano bissexto pode ser calculado verificando se ele é divisível por 4. Caso não seja divisível
por 4, ele não é bissexto. Caso seja divisível por 4, deve-se verificar se ele é divisível por 100. 
Caso não seja divisível por 100, ele é bissexto. Caso seja divisível por 100, deve-se verificar se 
ele é divisível por 400. Caso seja divisível por 400, ele é bissexto. Caso não seja divisível por 
400, ele não é bissexto. Escreva um programa que peça ao usuário que ele digite um ano e calcule 
se o ano digitado é bissexto ou não.
'''

ano = int(input('Digite o Ano: '))

if (ano%4 == 0):
    if(ano%100!=0):
        print('Ano Bissexto')
    else:
        if(ano%400==0):
            print('Ano Bissexto')
else:
    print('Nao e Bissexto')
