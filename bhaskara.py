import math


def delta (a, b, c):
     
    return b**2 - 4*a*c
    

print("Calculando as raízes da equação de segundo grau.")
print("Digite os valores de A, B,C")


entradas = input("Digite os valores separdos por um espaço: ").split(' ')
 
a = float(entradas [0])
b = float(entradas [1])
c = float(entradas [2])


#Calculando o delta
D = delta(a, b, c)

#tratando as saídas
if ((b**2 - 4*a*c) < 0) or (a == 0.0):

    print('Não existem raízes reais!')

elif D == 0:

    unica_raiz = (-b + math.sqrt(D))/(2*a) 

    print('Única raiz = {:.2f}'.format(unica_raiz))


else:
    x_1 = (-b + math.sqrt(D))/(2*a)
    x_2 = (-b - math.sqrt(D))/(2*a)

    print("x1 = {:.2f}".format(x_1))
    print("x2 = {:.2f}".format(x_2))



