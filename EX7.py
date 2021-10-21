''' Faça um programa que dados três valores X, Y e Z, verifica se eles podem ser os comprimentos 
dos lados de um triângulo e, se forem, verificar se é um triângulo equilátero, isósceles ou escaleno. 
Caso eles não formem um triângulo, escreva uma mensagem.
• Para verificar se as três medidas formam um triângulo, cada soma entre as medidas de 
dois lados deve ser maior que a terceiro lado.
o Lado A + Lado B > Lado C
o Lado A + Lado C > Lado B
o Lado B + Lado C > Lado A'''

X = float(input('Digite um valor para X: '))
Y = float(input('Digite um valor para Y: '))
Z = float(input('Digite um valor para Z: '))

if (X+Y>Z or X+Z>Y or Y+Z>X) and (X<=0 and Y<=0 and Z<=0):
    if(X==Y and X==Z and Y==Z):
        print('Triangulo Equilatero')
    if(X==Z and X!=Y) or (X==Y and X!=Z) or (Y==X and X!=Z):
        print('Triangulo Isosceles')
    if(X!=Y and X!=Z and Z!=Y):
        print('Triangulo Escaleno')
else:
    print('Nao forma um triangulo')