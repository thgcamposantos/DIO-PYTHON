# Crie uma classe chamada Animal que tenha um método chamado fazer_som(), que exiba a mensagem "O animal faz um som". Em seguida, crie uma classe derivada chamada Cachorro que sobrescreva o método fazer_som() para exibir "O cachorro late". Instancie um objeto de Cachorro e chame o método fazer_som().

# RESPOTA

# class Animal:
#     def fazer_som(self):
#         print("O animal faz um som")
# class Cachorro(Animal):
#     def fazer_som(self):
#         print("O cachorro late")
# cachorro = Cachorro()
# cachorro.fazer_som()

# Implemente uma classe base chamada Veiculo, com atributos marca e modelo. Crie um método chamado mostrar_info() que exibe a marca e o modelo. Depois, crie uma classe derivada chamada Carro, que adicione o atributo numero_portas. Modifique o método mostrar_info() para incluir o número de portas.

# RESPOSTA

class Veiculo:
    def __init__(self , marca , modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(self.marca , self.modelo)

class Carro(Veiculo):
    def __init__(self , marca , modelo , passageiros):
        super().__init__(marca , modelo)
        self.passageiros = passageiros
    
    def mostrar_info(self, marca, modelo , passageiro):
        print(f'Marca: {marca} / Modelo: {modelo} / Passageiro: {passageiro}')

gol = Carro("VW" , "Gol" , 4)
gol.mostrar_info("Vw" , "Gol" , 4)

# Implemente uma classe chamada Pessoa, com atributos como nome e idade, e um método cumprimentar() que exiba uma mensagem de cumprimento. Em seguida, crie uma classe Estudante que herde de Pessoa e adicione o atributo matricula. Sobrescreva o método cumprimentar() para incluir a matrícula no cumprimento.

# class Pessoa:
#     def __init__(self , nome , idade):
#         self.nome = nome
#         self.idade = idade
#     def cumprimentar(self):
#         print("Cumprimento")
# class Estudante(Pessoa):
#     def __init__(self , nome , idade , matricula):
#         super().__init__(nome , idade)
#         self.matricula = matricula
#     def cumprimentar(self , nome , matricula):
#         print(f'Cumprimento de {nome} MAT: {matricula}')
# Thiago = Estudante("Thiago" , 24 , 58777)
# Thiago.cumprimentar("Thiago" , 58777)

