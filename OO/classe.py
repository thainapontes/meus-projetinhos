class Pessoa: #a classe é Pessoa
    def __init__(self,peso,nome,idade): #init é o metodo construtor
        self.nome=nome #isso aq são os atributos
        self.peso=peso
        self.idade=idade

    def andar(self):
        print("Foi dormir")

p1= Pessoa(60,'Thainá',18)
p1.nome="Thainá Pontes" #quando já atribuiu um conteudo
print(Pessoa)