print ("Bem vindo!")

pergunta_nome = input("Qual é o seu nome? " )
whatsapp = input(f"Qual é o seu WhatsApp? ")
idade = input(f"Qual é a sua idade? ")
peso = float(input("Qual é o seu peso (em KG)? "))
altura = float(input("Qual é a sua altura (em metros e usando ponto)? "))

imc = (peso / (altura * altura))
consumo_agua = (float(peso) * 0.035)
	
print("Vamos aos resultados:")
print(pergunta_nome, (f"seu WhatsApp é: {whatsapp:},"),
	  (f"seu peso é: {idade:},"), 
	  (f"seu altura é: {altura:.2f} m,"), 
	  (f"seu consumo diário de água recomendado é de: {consumo_agua:.2f} l,") , 
	  (f"seu IMC é: {imc:.2f}, então sua condição atual é: ")) 

if imc <= 18.5:
	print("Abaixo do peso")
elif imc <= 25:
	print("Peso normal")
elif imc <= 30:
	print("Sobrepeso")
elif imc <= 35:
	print("Obesidade grau 1 (leve)")
elif imc <= 40:
	print("Obesidade grau 2 (moderada)")
else:
	print("Obesidade grau 3 (mórbida)")

#CRUD