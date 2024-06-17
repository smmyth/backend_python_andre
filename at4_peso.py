sexo = input(str("Digite M se for mulher ou H se for homem: "))
altura = float(input("Digite sua altura em metros: "))

peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7

if sexo.upper() == "H":
    print (f" H - O peso ideal para sua altura é: {peso_ideal_h:.2f}Kg")
else:
    print (f"F - O peso ideal para sua altura é: {peso_ideal_m:.2f}Kg")