# dame.danae.main.py
from grace.main import main as grace
from _spy.vitollino.main import Codigo
TEXTO = """ DIÁRIO DE PESQUISA
Se você encontrou este livro
é porque nesta casa aconteceu
um crime.
Preciso que você encontre as
outras páginas para podermos
solucionar este mistério
'''"""
TEXTO1 = """'''Se você encontrou este livro
é porque nesta casa aconteceu
um crime.
'''"""

class Livro:
    def __init__(self, casa):
        self.clica_livro = lambda: None
        _livro_fechado = "https://i.imgur.com/ty2fWuE.gif"
        _livro_aberto = "https://i.imgur.com/sI177hV.jpg"
        self.casa = casa()
        self.casa.vit.i.inicia()
        livro = self.casa.vit.a(_livro_fechado, "caderno de notas",
            style=dict(left=280, top=500, width=60, height="60px"))
        cena_livro = self.casa.vit.c(_livro_aberto, self, self)
        livro.entra(self.casa.sala.B.leste)
        texto = Codigo(
             codigo=TEXTO1, topo=TEXTO,
             vai=self.vai, style=dict(left=450, top=10, width=400))
        texto.entra(cena_livro)
        def abre_livro(*_):
            self.clica_livro = lambda: None
            cena_livro.vai()
        def pega_livro(*_):
            self.clica_livro = abre_livro
            self.casa.vit.i.bota(livro)
        self.clica_livro = pega_livro
        livro.vai = lambda *_: self.clica_livro()
        
    def vai(self, *_):
        self.clica_livro = abre_livro
        self.casa.vit.i.cena.vai()


def main(bry=grace):
    return Livro(bry)


if __name__ == '__main__':
    main(grace)
