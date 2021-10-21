'''Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 
km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da 
multa, cobrando R$ 5 por km acima de 80 km/h.'''

Velocidade = float(input('Qual a velocidade do seu carro? '))
valorMulta = (Velocidade - 80) * 5
if Velocidade > 80:
    print('O senhor foi MULTADO!')
    print('Valor da multa R$', valorMulta)