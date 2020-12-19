
# Função para gerar números aleatórios
def genRandomNumbers():
	try:
		from random import randint		#Importa o pacote para gerar números inteiros aleatórios
		cpf = [] 						#Cria um array list chamado cpf
		for number in range(9): 		#Laço for para gerar 9 números aleatórios
			cpf.append(randint(0, 9)) 	#Gera e inclui o número gerado no array cpf

		return cpf 						#Retorna cpf
	except ImportError:
		raise ImportError('Não foi possível importar o pacote') #Gera um erro caso não de para importar o pacote random

# Transforma uma string em uma lista
def strToList(string):
	NewList = [] 					#Cria um array list chamado NewList
	for el in string:				# Laço for (Para cada caracter contido na string passada no parametro ele armazena aquele caracter na variavel "el")
		NewList.append(int(el))		#Transforma a variavel el em inteiro e adiciona na lista
	return NewList					# retorna a lista

# Transforma uma lista em uma string
def listToStr(list):
	'''
		Funciona da mesma forma da função acima mas trabalha da maneira inversa
		pega os valor do array e acrescenta na string
	'''

	newString = ''
	for el in list:
		newString+=str(el)
	return newString


'''
	Calc é a função principal do código
	Recebe o parametro first Calc obrigatorio
	e algum outro parametro opcional


	@param: firstCalc = Verifica se é a primeira  vez que o código está rodando
	@param: *args = Armazena qualquer outra variavel em uma array tuple chamada args - Nesse caso armazena o CPF
'''

def Calc(firstCalc, *args):
	count = 10		#Contador inicia em 10 para começar os calculos do digito validador
	nonVerifiedCPF = genRandomNumbers()	# Gerar os 9 digitos base do cpf
	if args:			# Se foi informado algo no *args ele pega o valor e salva em nonVerifiedCPF
		nonVerifiedCPF = args[0]
	if not firstCalc:	# Se for o segundo calculo contador recebe 11
		count = 11
	soma = 0
	while count >= 2: # Enquanto contador for maior ou igual a dois 
		for number in nonVerifiedCPF:	# Para cada numero no cpf
			soma += number*count		# soma recebe soma mais numero * contador (soma = soma + numero * numero )
			count -= 1					# contador = contador - 1
	

	if soma%11 < 2:  # Se o modulo da sama por 11 for menor que 2 adiciona 0 ao digito validador
		nonVerifiedCPF.append(0)
	else:			# se não adiciona 11 menos o modulo da soma por 11
		nonVerifiedCPF.append(11-(soma%11))
	if firstCalc:
		n = Calc(False, nonVerifiedCPF)
		n.insert(3, '.')
		n.insert(7, '.')
		n.insert(11, '-')
		return listToStr(n)
	else:
		return nonVerifiedCPF


def init():
	print(' Gerador de CPF ')

	# Pega o CPF que o usuário digitar
	cpf = input(' Digite um número com 9 digitos para ser gerado os digitos validadores: (Prescione Enter para números aleátorios) \n')



	if len(cpf) <= 0: 				# Verifica o tamanho da string cpf pega acima, se for menor que zero
		validatedCPF = Calc(True) 	# Chama a função Calc passando True como primeiro parametro e 
		print(validatedCPF)			#armazena o resultado na variavel validatedCPF
		init()						# Chama a função init para começar denovo

	else:							
		for caracter in cpf:		# para cada caracter em cpf


			# Verifica se todos os caracteres são números
			try:
				caracter = int(caracter) 		#Tenta transforma o caracter em questão em inteiro
			except ValueError:			# Se não transformar em inteiro gera o erro ValueError
				print('Digite apenas números') #Exibe o erro
				init()			#executa a função init para começar denovo
		if len(cpf) is not 9:	# Se o tamanho for diferente de 9, gera erro e executa denovo
			print('Digite 9 números')
			init()
		else:					# Se for igual a 9

			validatedCPF = Calc(True, strToList(cpf)) # Chama a função Calc e passa o parametro True e o cpf digitado pelo user
			print(validatedCPF)
			init()
init()
