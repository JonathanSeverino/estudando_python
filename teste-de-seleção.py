values = input().split(' ')

numeros = [ int(numeros) for numeros in values]

a, b, c, d = numeros


if ((b > c) and (d > a) and (c + d) > (a + b) and (c > 0 and d > 0 )and (a % 2 == 0)):
        
        print("Valores aceitos")

else:
        print("Valores nao aceitos")