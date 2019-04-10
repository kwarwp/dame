# dame.danae.main.py
from grace.main import main as grace
from _spy.vitollino.main import Codigo
DNA = "https://i.imgur.com/tEtZk2X.jpg"

TEXTO = ["""<div style="width:100%; text-align: center;">
<H2>DIÁRIO DE EMERGÊNCIA</H2>
<br>
<img src="https://i.imgur.com/tEtZk2X.jpg" width=200 />
</div>
<br/><br/>
Caro visitante, desculpe a intromissão
no seu lazer, espero contar com a sua ajuda.
Se você encontrou este livro
é porque nesta casa aconteceu
um crime.<br/>
Preciso que você encontre as
outras páginas, que por segurança foram
espalhadas por esta casa. E por segurança
dobrada, as suas informações foram encobertas por enigmas. 
Por favor, ache as soluções para podermos
solucionar este mistério
""",
"""<div style="width:100%; text-align: center;">
<H2>Página 1 Ácido Desoxirribonucleico</H2>
<br>
<img src="https://i.imgur.com/TMzO0uw.jpg" width=300 />
</div>
<br/><br/>
O DNA (ácido desoxirribonucleico) é um
tipo de ácido nucleico que possui
destaque por armazenar a informação
genética da grande maioria dos seres
vivos. Essa molécula é formada por
nucleotídeos e apresenta,geralmente,
a forma de uma dupla-hélice. Nos
organismos eucarióticos,o DNA é
encontrado no núcleo da célula, nas
mitocôndrias e nos cloroplastos.
Nos procariontes, o DNA está localizado
em uma região que não é delimitada por
membrana, denominada de nucleoide.
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
        self.pagina_final = 0
        class PaginaAnterior:
            def __init__(self, livro):
                self.livro = livro
            def vai(self, *_):
                if self.pagina_atual == 0:
                    self.livro.fecha_livro()
                    return False
                self.livro.pagina_atual -= 1
                self.livro.texto.topo.html = TEXTO[self.livro.pagina_atual]
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
        cena_livro = self.casa.vit.c(_livro_aberto, PaginaAnterior(self), self)
        livro.entra(self.casa.sala.B.leste)
        self.texto = texto = Codigo(
             codigo="", topo=TEXTO[0],
             vai=self.pagina, style=dict(left=440, top=20, width=380))
        texto.entra(cena_livro)
        def abre_livro(*_):
            self.clica_livro = lambda: self.fecha_livro()
            self.onde = self.casa.vit.i.cena
            cena_livro.vai()
        def pega_livro(*_):
            self.clica_livro = abre_livro
            self.casa.vit.i.bota(livro)
        self.abre_livro = abre_livro
        self.clica_livro = pega_livro
        livro.vai = lambda *_: self.clica_livro()
        class Aviso:
            def __init__(self, vit):
                porta = vit.sala.C.sul
                self.aviso = vit.n(porta, "Esta Porta Está Trancada")
                porta.meio = self
            def vai(self, *_):
                self.aviso.vai()
        aviso = Aviso(self.casa.vit)
        class Pagina:
            def __init__(self, vit, nova):
                quadro = vit.sala.B.sul
                self.aviso = vit.n(quadro, "Você acha uma folha e cola no caderno", foi=nova)
                self.papel = vit.a("https://i.imgur.com/d1nyTmx.jpg",
                    style=dict(left=440, top=500, width=4), cena=quadro, vai=self.vai)
            def vai(self, *_):
                self.aviso.vai()
                self.casa.vit.i.bota(self.papel)
                event.stopPropagation()
        pagina = Pagina(self.casa.vit, self.pagina)
        
    def pagina(self, event, *_):
        self.pagina_atual = 1
        self.pagina_final = 1
        event.stopPropagation()
        
    def fecha_livro(self, *_):
        self.clica_livro = self.abre_livro
        self.onde.vai()
        
    def vai(self, *_):
        if self.pagina_atual == self.pagina_final:
            self.fecha_livro()
            return False
        self.pagina_atual += 1
        self.texto.topo.html = TEXTO[self.pagina_atual]


def main(bry=grace):
    return Livro(bry)


if __name__ == '__main__':
    main(grace)
