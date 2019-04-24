import math


def delta (a, b, c):
     
    return b**2 - 4*a*c
    

print("Calculando as raízes da equação de segundo grau.")
print("Digite os valores de A, B,C")


a = float(input('A = '))
b = float(input('B = '))
c = float(input('C = '))


#Calculando o delta
D = delta(a, b, c)

#tratando as saídas
if D < 0:

    print('Não existem raízes reais!')

if D == 0:

    unica_raiz = (-b + math.sqrt(D))/(2*a) 

    print('Única raiz = {:.2f}'.format(unica_raiz))


if D > 0:
    x_1 = (-b + math.sqrt(D))/(2*a)
    x_2 = (-b - math.sqrt(D))/(2*a)

    print("x1 = {:.2f}".format(x_1))
    print("x2 = {:.2f}".format(x_2))



