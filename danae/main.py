# dame.danae.main.py
from grace.main import main as grace
from _spy.vitollino.main import Codigo
DNA = "https://i.imgur.com/tEtZk2X.jpg"

TEXTO = ["""<div style="width:100%; text-align: center;">
<H2>DIÁRIO DE PESQUISA</H2>
<br>
<img src="https://i.imgur.com/tEtZk2X.jpg" width=200 />
</div>
<br/><br/>
Se você encontrou este livro
é porque nesta casa aconteceu
um crime.<br/>
Preciso que você encontre as
outras páginas para podermos
solucionar este mistério
""",
"""<div style="width:100%; text-align: center;">
<H2>Página 1</H2>
<br>
<img src="https://i.imgur.com/tEtZk2X.jpg" width=200 />
</div>
<br/><br/>
Se você encontrou este livro
é porque nesta casa aconteceu
um crime.<br/>
Preciso que você encontre as
outras páginas para podermos
solucionar este mistério
""",
"""<div style="width:100%; text-align: center;">
<H2>Página 2</H2>
<br>
<img src="https://i.imgur.com/tEtZk2X.jpg" width=200 />
</div>
<br/><br/>
Se você encontrou este livro
é porque nesta casa aconteceu
um crime.<br/>
Preciso que você encontre as
outras páginas para podermos
solucionar este mistério
"""
]
TEXTO1 = """'''Se você encontrou este livro
é porque nesta casa aconteceu
um crime.
'''"""

class Livro:
    def __init__(self, casa):
        self.pagina_atual = 0
        class PaginaAnterior:
            def vai(self, *_):
                self.pagina_atual -= 1
                self.texto.topo.html = TEXTO[self.pagina_atual]
        class PaginaPosterior:
            def vai(self, *_):
                self.pagina_atual += 1
                self.texto.topo.html = TEXTO[self.pagina_atual]
        self.clica_livro = lambda: None
        self.onde = None
        _livro_fechado = "https://i.imgur.com/ty2fWuE.gif"
        _livro_aberto = "https://i.imgur.com/sI177hV.jpg"
        self.casa = casa()
        self.casa.vit.i.inicia()
        livro = self.casa.vit.a(_livro_fechado, "caderno de notas",
            style=dict(left=280, top=500, width=60, height="60px"))
        cena_livro = self.casa.vit.c(_livro_aberto, PaginaAnterior(), PaginaPosterior())
        livro.entra(self.casa.sala.B.leste)
        self.texto = texto = Codigo(
             codigo=TEXTO1, topo=TEXTO,
             vai=self.pagina, style=dict(left=440, top=20, width=380))
        texto.entra(cena_livro)
        def abre_livro(*_):
            self.clica_livro = lambda: self.vai()
            self.onde = self.casa.vit.i.cena
            cena_livro.vai()
        def pega_livro(*_):
            self.clica_livro = abre_livro
            self.casa.vit.i.bota(livro)
        self.abre_livro = abre_livro
        self.clica_livro = pega_livro
        livro.vai = lambda *_: self.clica_livro()
        
    def pagina(self, event, *_):
        self.texto1.vai()
        event.stopPropagation()
        
    def vai(self, *_):
        self.clica_livro = self.abre_livro
        self.onde.vai()


def main(bry=grace):
    return Livro(bry)


if __name__ == '__main__':
    main(grace)
