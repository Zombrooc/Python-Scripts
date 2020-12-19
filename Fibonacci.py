primeiro_valor = 1
segundo_valor = 1
resultado = 0
while True:
	resultado = primeiro_valor + segundo_valor
	segundo_valor = primeiro_valor
	primeiro_valor = resultado
	print(resultado)
