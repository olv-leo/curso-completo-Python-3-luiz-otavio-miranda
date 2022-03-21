from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        self.alimento = alimento
        print(f'{self.nome} está comendo {self.alimento}.')
        self.comendo = True

    def parar_comer(self):
        print(f'{self.nome} parou de comer.')
        self.comendo = False
        self.alimento = ""

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        self.assunto = assunto
        print(f'{self.nome} está falando sobre {self.assunto}')
        self.falando = True

    def parar_falar(self):
        print(f'{self.nome} parou de falar.')
        self.falando = False
        self.assunto = ""

    def ano_nascimento(self):
        print(f'{self.nome} nasceu em: {self.ano_atual - self.idade}')

if __name__ == '__main__':
    p1 = Pessoa('Leonardo', 25)

    p1.comer('maçã')
    p1.falar('POO')
    p1.parar_comer()
    p1.falar('POO')
    p1.comer('arroz')
    p1.parar_falar()
    p1.falar('Python')
    p1.ano_nascimento()