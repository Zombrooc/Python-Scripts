from time import sleep
from os import system


def Retangulo(b, h):
	return b*h


def Cilindro(r, h):
	C = 2*3.14*r # C*h == Área Lateral
	Ac = 3.14*r**2 # Área da Base == Área do Circulo
	At = 2*Ac+(Retangulo(C, h))
	V = Ac * h
	return Ac, At, C, V


def Medida(valor):
	while True:
		print('Digite a medida desejeda: ')
		print(' [ 1 ] - M')
		print(' [ 2 ] - Cm')
		opcao = int(input('Digite a opção: '))
		
		if opcao == 1:
			print('Volume: {}m³'.format('%.2f' % valor))
			print('Volume: {}L\n'.format(valor*1000))
			return 0
		elif opcao == 2:
			print('Volume: {}cm³'.format(valor))
			print('Volume: {}L\n'.format(int(valor*0.001)))
			return 0
		else:
			print('Digite uma opção válida...')


def Cone(h, r, g):
	g = g
	h = h
	r = r
	if g == 0:
		g = h**2+r**2
		g = g**(1/2)
	
	if r == 0:
	    r = g/2
	
	if h == 0:
		h = g**2-r**2
		h = h**(1/2)
	
	Ab = r**2
	Al = r*g
	At = ((r*g)+(r**2))
	V = (r**2*h)/3
	return Ab, g, Al, At, V, h, r


def inicio():
	while True:
		print(' [ 1 ]  - Calcular Cilindro')
		print(' [ 2 ]  - Calcular Cone')
		opcao = input('Digite um opção: ')
		try:
			opcao = int(opcao)
			if opcao == 1:
				Raio = float(input('Digite o raio do Cilindro: '))
				Altura = float(input('Digite a Altura do Cilindro: '))
				cilindro = Cilindro(Raio, Altura)

				print('Área da Base: {}'.format(cilindro[0]))
				print('Área Total: {}'.format(cilindro[1]))
				print('Circunferência: {}'.format('%.2f' % cilindro[2]))
				Medida(cilindro[3])
				sleep(2)
			elif opcao == 2:
				Altura = float(input('Digite a altura: (Use 0 para valor não informado)'))
				Raio = float(input('Digite o raio: (Use 0 para valor não informado)'))
				Geratriz = float(input('Digite a Geratriz: (Use 0 para valor não informado)'))
				cone = Cone(Altura, Raio, Geratriz)

				print('Área da Base: {} pi'.format('%.2f' % cone[0]))
				print('Área Total: {} pi'.format('%.2f' % cone[3]))
				print('Geratriz: {}'.format('%.2f' % cone[1]))
				print('Área Lateral: {} pi'.format('%.2f' % cone[2]))
				print('Altura: {}'.format('%.2f' % cone[5]))
				print('Raio: {}'.format('%.2f' % cone[6]))
				Medida(cone[4])
				sleep(2)
			elif opcao == 0:
				system('cls')
			else:
				print('Digite uma opção Válida')
		except ValueError:
			print('Digite apenas números...')


inicio()
