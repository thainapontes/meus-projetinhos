class Pessoa:
    def __init__(self,nome,peso,idade,comer=False,andar=False,dormir=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
        self.andando=andando
        self.dormindo=dormindo

    def andar(self): #pra ele andar, precisa verificar se ele n está comendo e dormindo
        if self.andando==False:
                if self.comendo==False:
                        if self.dormindo==False:
                                self.andando = True
                                print('Foi andar')
    def comer(self):
        if self.comendo==False:
                if self.andando==False:
                        if self.dormindo==False:
                                print('Foi comer.')

    def dormir(self):
        if self.comendo==False:
                if self.andando==False:
                        if self.dormindo==False:
                                print('Foi dormir.')




   #pessoa = Pessoa()
   #pessoa.nome