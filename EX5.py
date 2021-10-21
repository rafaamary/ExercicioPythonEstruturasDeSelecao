''' Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para 
indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
'''
qtdkWh = float(input('Qual a quantidade de kWh consumida? '))
tipoInst = str(input('Qual o tipo de instalacao? '))
if (qtdkWh <= 500 and tipoInst == 'R'):
    preco = 0.40
elif (qtdkWh > 500 and tipoInst == 'R'):
    preco = 0.65
elif (qtdkWh <=1000 and tipoInst=='C'):
    preco = 0.55
elif (qtdkWh > 1000 and tipoInst == 'C'):
    preco = 0.60
elif (qtdkWh <=5000 and tipoInst=='I'):
    preco = 0.55
elif(qtdkWh > 5000 and tipoInst=='I'):
    preco = 0.60 
print('O preco e: R$', qtdkWh*preco)