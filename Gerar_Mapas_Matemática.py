from random import randrange
quadrados = []
j = 1
while j < 999:
	lista = []
	for i in range(1, 5):
		coresCopia = ['V', 'P', 'A', 'B']
		if i is 1:
			lista.append(coresCopia[randrange(4)])
		elif i is 2:
			coresCopia = ['V', 'P', 'A', 'B']
			coresCopia.remove(lista[0])
			lista.append(coresCopia[randrange(len(coresCopia))])
		elif i is 3:
			coresCopia = ['V', 'P', 'A', 'B']
			coresCopia.remove(lista[0])
			lista.append(coresCopia[randrange(len(coresCopia))])
		elif i is 4:
			coresCopia = ['V', 'P', 'A', 'B']
			if lista[1] != lista[2]:
				coresCopia.remove(lista[1])
				coresCopia.remove(lista[2])
				lista.append(coresCopia[randrange(len(coresCopia))])
			else:
				coresCopia.remove(lista[1])
				lista.append(coresCopia[randrange(len(coresCopia))])
	
	if lista not in quadrados:
		quadrados.append(lista)
	j+=1


print(len(quadrados))
for el in quadrados:
	print('''
			############################
			#            #             #
			#      {}     #      {}      #
			#            #             #
			############################
			#            #             #
			#      {}     #      {}      #
			#            #             #
			############################

		'''.format(el[0], el[1], el[2], el[3]))