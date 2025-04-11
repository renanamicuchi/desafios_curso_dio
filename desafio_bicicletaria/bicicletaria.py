class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor # self é uma referência de instância do objeto que foi passado.
        self.modelo = modelo # self. com esse ponto chamamos de atributos da classe.
        self.ano = ano
        self.valor = valor
        

    def buzinar(self):
        print("Plim, Plim...")

    def parar(self):
        print("parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.
        __dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 200)
print(b2)
b2.correr()

#b2.buzinar() # seria mesma coisa que colocar: Bicicleta.buzinar(b2)