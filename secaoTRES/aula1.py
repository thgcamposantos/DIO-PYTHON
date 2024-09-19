class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):  # Corrigido para __init__
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('som de buzina')

    def parar(self):
        print('Parando Bicicleta')

    def correr(self):
        print('Parando Bicicleta')  # Corrigido erro de digitação aqui também

b1 = Bicicleta('branca', 'caloi', 2020, 300)
b1.buzinar()
