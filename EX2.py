''' Escreva um programa que leia três números e que imprima o maior e o menor'''

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

if (n1 > n2 and n1 > n3) and (n2 < n1 and n2 < n3):
    print('Maior: ', n1 )
    print('Menor: ', n2)
elif (n1>n2 and n1>n3) and (n3<n1 and n3<n1):
    print('Maior: ', n1)
    print('Menor: ', n3)
elif(n2>n1 and n2>n3) and (n1<n2 and n1<n3):
    print('Maior: ', n2)
    print('Menor: ', n1)
elif (n2>n1 and n2>n3) and (n3 < n1 and n3 < n2):
    print('Maior: ', n2)
    print('Menor: ', n3)
elif (n3 > n1 and n3 > n2) and (n1 < n2 and n1 < n3):
    print('Maior: ', n3)
    print('Menor: ', n1)

else:
    print('Maior: ', n3)
    print('Menor: ', n2)

'''maior = n1
if (n2 > maior):
    maior = n2
elif (n3 > maior):
    maior = n3
print('Maior: ', maior)

menor = n1
if (n2 < menor):
    menor = n2
elif (n3 < menor):
    menor = n3
print('Menor: ', menor)'''