# dame.danae.main.py
from grace.main import main as grace


class Livro:
    def __init__(self, casa):
        self.clica_livro=lambda: None
        _livro_fechado = "https://i.imgur.com/ty2fWuE.gif"
        _livro_aberto = "https://i.imgur.com/sI177hV.jpg"
        self.casa = casa()
        self.casa.vit.i.inicia()
        livro = self.casa.vit.a(_livro_fechado, "caderno de notas")
        cena_livro = self.casa.vit.c(_livro_aberto, self, self)
        livro.entra(self.casa.sala.B.leste)
        def abre_livro(*_):
            cena_livro.vai()
        def pega_livro(*_):
            self.clica_livro=abre_livro
            self.casa.vit.i.bota(livro)
        self.clica_livro = pega_livro
        livro.vai = self.clica_livro
        
    def vai(self, *_):
        self.casa.vit.i.cena.vai()


def main(bry=grace):
    return Livro(bry)


if __name__ == '__main__':
    main(grace)
