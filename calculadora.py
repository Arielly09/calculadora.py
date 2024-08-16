class Calculadora: 

    def adicionar(self, a, b):
        return a+b

    def subtrair(self, a, b):
        return a-b

    def multiplicar(self, a, b):
        return a*b

    def dividir(self, a, b):
        if b ==0:
            return "Erro: Divisão por zero não é permitida"
        return a/b

    def restoDaDivisao(self, a, b):
        return a%b 

c = Calculadora()
print("soma:", c.adicionar(10,5))
print("subtração:", c.subitrair(10,5))
print("multiplicação:", c.multiplicar(10,5))
print("divisão:", c.dividir(10,5))
print("resto da divisão:", c.restoDaDivisao(10,5))