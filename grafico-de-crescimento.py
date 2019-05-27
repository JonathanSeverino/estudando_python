#Gráfico de crescimento da população brasileira 1980-2016

import matplotlib.pyplot as plt 

dados = open("populacao-brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))




plt.bar(x, y, color ="blue")
plt.plot(x, y, color ='k', linestyle = '--')

plt.title = "crescimento da população brasileira 1980-2016"
plt.xlabel= "ANOS"
plt.ylabel = "População x 100.000.000"


#plt.show()

#salvando imagem
plt.savefig('populacao-brasileira.pdf')


