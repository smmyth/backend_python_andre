escolha1 = float(input('Digite o primeiro número: '))
escolha2 = float(input('Digite o segundo número: '))
print(('A soma dos números é:'), escolha1 + escolha2)

par_ou_impar = int(input('Digite o número: '))
if par_ou_impar % 2 == 0:
 print("O número é par.")
else:
 print("O número é ímpar.")

numeros = [3, 6, 8, 10]
print("O maior é:", max(numeros))

temperatura = float(input('Digite a temperatura em Fahrenheit: '))
celsius = ((temperatura - 32) / 1.8)
print(f'A temperatura em Celsius é: {celsius:.2f}ºC')


sinal_numero = float(input('Digite o número para verificação: '))
if sinal_numero < 0:
	print("O número é negativo.")
elif sinal_numero == 0:
	print("O número é zero.")
else:
	print("O número é positivo.")
