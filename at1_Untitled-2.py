class Paciente:
    def __init__(self, nome, whatsapp, peso, altura):
        self.nome = nome
        self.whatsapp = whatsapp
        self.peso = peso
        self.altura = altura
    
    def consumo_agua(self):
        # Consumo de água recomendado: 35 ml por kg de peso corporal
        return self.peso * 0.035
    
    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    
    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau 1 (leve)"
        elif 35 <= imc < 39.9:
            return "Obesidade grau 2 (moderada)"
        else:
            return "Obesidade grau 3 (mórbida)"
    
    def __str__(self):
        imc = self.calcular_imc()
        classificacao = self.classificar_imc()
        consumo = self.consumo_agua()
        return (f"Nome: {self.nome} - WhatsApp: {self.whatsapp}, Peso: {self.peso}kg - Altura: {self.altura}m "
                f"- Consumo de água diário: {consumo:.1f} litros - IMC: {imc:.1f} - Nível de obesidade: {classificacao}.")
