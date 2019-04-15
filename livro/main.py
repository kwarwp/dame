# dame.livro.main.py
# dame.danae.main.py
from sherlock.main import main as sherlock
from random import shuffle
# from browser import html

DICT = {}
COLA_NO_CADERNO = "Você acha uma folha e cola no caderno"
ENIGMA1 = "á?ido,#desoxirribonuc?eico,#t?po,#???ÂÂÂ possui,#armaze??r,#" \
          "in?ormação,#genét?ca,#?rande,#moléc?la,#fo?m??aÂÂÂ p?r,#nu?leotídeos,#" \
          "ap?esenta,#f?r?a,#?rgani?mo?,#eucariótic?s,#?it?côndrias".split("#")

DNA = "https://i.imgur.com/tEtZk2X.jpg"

TEXTO = [
    """<div style="width:100%; text-align: center;">
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
    <H2>2 Os Cromossomos</H2>
    <br>
    <img src="https://i.imgur.com/mdHOJ9y.jpg" width=200 onclick="clica_elemento()"/>
    </div>
    <br/>
    Cromossomos são estruturas compostas de DNA que,
    por sua vez, carregam os genes de um ser vivo,
    responsáveis por definir as características físicas
    particulares de cada indivíduo.
    <br/>
    Os cromossomos estão localizados no núcleo das
    células do ser vivo. Os seres humanos
    possuem 46 cromossomos, divididos em 23 pares,
    sendo 44 autossomos e 2 sexuais.
    <br/><br/><span style="color:#FF0000;">
    Decifre o enigma para obter uma pista:</span><br/><br/>
    {}
    
    """,
    """<div style="width:100%; text-align: center;">
    <H2>Página 3 Os Genes</H2>
    <br>
    <img src="https://i.imgur.com/EXNWAPb.png" width=200 />
    </div>
    <br/><br/>
    Um gene é o menor fragmento de uma molécula de ADN (DNA) que possui
    informação completa para um caráter determinado.    <br/>
    Cada gene codifica uma determinada sequência de uma cadeia
    polipeptídica (união de aminoácidos que formam a proteína).
    O gene é formado por uma sequência de DNA
    (ácido desoxirribonucleico) e RNA (ácido ribonucleico),
    sendo este último responsável pela síntese de proteínas da célula.
    <br/>
    Um gene é constituído por vários fragmentos de ADN separados
    por sequências sem sentido.
    As parte com sentido servem para fabricar a proteína são denominadas
    Exons e as partes sem sentido intercaladas no gene, Introns.
    """

]
shuffle(ENIGMA1)
TEXTO[2] = TEXTO[2].format(" ".join(
    '<span style="color:#FF0000;">{}</span>'.format(w) for w in ENIGMA1))


class Livro:
    jogo = None

    def __init__(self, jogo, sherlock_=sherlock):
        self.pagina_atual = 0
        self.pagina_final = 0
        self.jogo = jogo
        self.cena_livro_aberto = None
        self.clica_livro = self.abre_livro = lambda: None
        self.cena_onde_estou_no_jogo = None
        self.texto_da_pagina_do_livro = self.jogo.codigo(
            codigo="", topo=TEXTO[0],
            style=dict(left=440, top=20, width=380))
        sherlock_(jogo)
        jogo.i.inicia()
        self.cria_o_livro()
        cromo = self.cria_pagina(vai=lambda: self.cria_pagina(
                quadro=self.jogo.sala.A.sul, tit="pagina2", left=310, top=340))
        jogo.clica_elemento = cromo.chave_cromossomo
        cromo.chave_cromossomo(cena=self.jogo.sala.A.norte)

    def cria_o_livro(self):

        class PaginaAnterior:
            def __init__(self, livro_):
                self.livro = livro_

            def vai(self, *_):
                print("PaginaAnterior", self.livro.pagina_atual)
                if self.livro.pagina_atual == 0:
                    self.livro.fecha_livro()
                    return False
                self.livro.pagina_atual -= 1
                self.livro.texto_da_pagina_do_livro.topo.html = TEXTO[self.livro.pagina_atual]

        _livro_fechado = "https://i.imgur.com/ty2fWuE.gif"
        _livro_aberto = "https://i.imgur.com/sI177hV.jpg"
        livro = self.jogo.a(_livro_fechado, tit="caderno de notas",
                            style=dict(left=280, top=500, width=60, height="60px"))
        livro.entra(self.jogo.sala.B.leste)
        self.cena_livro_aberto = cena_livro = self.jogo.c(_livro_aberto, PaginaAnterior(self), self)
        self.texto_da_pagina_do_livro.entra(cena_livro)

        def abre_livro(*_):
            self.clica_livro = lambda: self.fecha_livro()
            self.cena_onde_estou_no_jogo = self.jogo.i.cena
            cena_livro.vai()

        def pega_livro(*_):
            self.clica_livro = abre_livro
            livro.img.title = "caderno, clique para abrir"
            self.jogo.i.bota(livro)

        self.abre_livro = abre_livro
        self.clica_livro = pega_livro
        livro.vai = lambda *_: self.clica_livro()

    def clica_elemento(self):
        pass

    def cria_aviso(self, cena=None, msg="Esta Porta Está Trancada", tit="", foi=lambda: None):
        cena = cena if cena else self.jogo.i.cena

        class Aviso:
            def __init__(self, cena_=cena, tit_=tit, msg_=msg, jogo=self.jogo, foi_=foi):

                self.aviso = jogo.n(cena_, tit_, msg_, foi=foi_)
                cena_.meio = self

            def vai(self, *_):
                self.aviso.vai()

        return Aviso(cena)
        
    def cria_pagina(self, **kwargs):

        class Pagina:
            def __init__(self, quadro=self.jogo.sala.B.sul, tit="pagina1", left=160, top=530,
                         width=16, height="60px", aviso=COLA_NO_CADERNO, vai=lambda: object(), livro=self):
                self.livro, self.jogo, self.tit, self.agora_vai = livro, livro.jogo, tit, vai
                self.height, self.left, self.top, self.width = height, left, top, width
                self.quadro, self.tit, self.papel = quadro, tit, None
                self.aviso = self.jogo.n(quadro, aviso)  # , foi=livro)
                self.cria_papel()

            def cria_papel(self,):
                self.papel = self.jogo.a(
                    "https://i.imgur.com/YqUFpx4.jpg", tit=self.tit,
                    # "https://i.imgur.com/YU3IFrt.jpg", tit=tit,
                    style=dict(left=self.left, top=self.top, width=self.width, height=self.height),
                    cena=self.quadro, vai=self.vai)

            def chave_cromossomo(self, _=None, cena=None):
                aviso = self.livro.cria_aviso(
                    cena=cena if cena else self.livro.cena_livro_aberto,  # foi=cria_chave,
                    tit="Use este cartão para abrir um baú.", msg="Arraste o cartão até a fechadura.")
                aviso.vai()

                chave = self.livro.cria_arrastante(cena=self.jogo.i,
                    drag=True, img="https://i.imgur.com/mdHOJ9y.jpg", tit="cartao que abre bau", vai=aviso.vai)
                self.jogo.clica_elemento = lambda *_: None
                self.livro.cria_arrastante(
                    drags = {"cartao que abre bau": lambda a=aviso: a.vai()},
                    drop=True, drag=False, img="https://i.imgur.com/3V2OwVV.png", tit="arraste o cartão aqui",
                    style=dict(left=500, top="400px", width=50, height="80px"),
                    cena=self.jogo.sala.C.leste, vai=aviso.vai)

            def vai(self, event=None):
                self.aviso.vai()
                self.jogo.i.bota(self.papel)
                self.jogo.i.tira(self.tit)
                self.livro.pagina_final += 1
                self.livro.pagina_atual += 1
                self.agora_vai()
                # self.nova.pagina_atual = 1
                event.stopPropagation() if event else None

        return Pagina(**kwargs) if kwargs else Pagina

    def nova_pagina(self, event=None):
        self.pagina_atual += 1
        self.pagina_final += 1
        event.stopPropagation() if event else None

    def fecha_livro(self, *_):
        self.clica_livro = self.abre_livro
        self.cena_onde_estou_no_jogo.vai()

    def vai(self, *_):
        if self.pagina_atual == self.pagina_final:
            self.fecha_livro()
            return False
        self.pagina_atual += 1
        self.texto_da_pagina_do_livro.topo.html = TEXTO[self.pagina_atual]

    def cria_arrastante(self, **kwargs):

        class Elemento(self.jogo.a):

            def __init__(self, img="", tit="", cena=None, drag=True, drop=False, drags=None, jogo=self.jogo, **_kwargs):
                super().__init__(tit=f"{tit}", **_kwargs)
                self._drag = self._over = self._drop = self._dover = self.vai = lambda *_: False
                self.jogo = jogo
                elt_style = {"background-image": f"url('{img}')", "background-size": "cover", "cursor": "move"}
                inv_style = {'opacity': "inherited", 'width': 30, 'height': "30px",
                             'min-height': '30px', 'float': 'left', 'position': 'unset'}
                self.style.update(elt_style)
                self.style.update(inv_style if (cena == self.jogo.i) else {})
                self.entra(cena) if cena else None
                # self.style = elt_style
                # self.scorer, self.xy = {}, 0
                # self.elt = html.DIV(Id=tit, title=tit, style=self.style)
                self.elt.style = self.style
                # self.img.id = tit

                self.elt.onclick = self._click
                self.elt.bind("dragstart", lambda ev: self._drag(ev))
                self.elt.onmouseover = lambda ev: self._dover(ev)
                self.elt.ondrop = lambda ev: self._drop(ev)
                self.elt.ondragover = lambda ev: self._over(ev)
                """
                self.img.onclick = self._click
                self.img.ondragstart = lambda ev: self._drag(ev)
                self.img.onmouseover = lambda ev: self._over(ev)
                self.img.ondrop = lambda ev: self._drop(ev)
                self.img.ondragover = lambda ev: self._dover(ev)

                """
                self.do_drag(drag)
                self.do_drop(drop)
                self.drags = drags if drags else DICT

            def foi(self):
                self._do_foi()

            def _do_foi(self):
                self.do_drag(False)
                self._do_foi = lambda *_: None

            @property
            def tit(self):
                return self.elt.title

            @tit.setter
            def tit(self, texto):
                self.elt.title = texto

            @staticmethod
            def _click(ev):
                _ = ev
                print("def _click(ev):")
                return False

            @staticmethod
            def mouse_over(ev):
                # ev.preventDefault()
                print("def drag_start(ev)mouse_over:", ev.target.id)
                ev.target.style.cursor = "move"
                return False

            def drag_start(self, ev):
                # ev.preventDefault()
                print("def drag_start(ev):", ev.target.id)
                ev.data['text'] = ev.target.id
                ev.data.effectAllowed = 'move'
                # ev.dataTransfer.setData("text", ev.target.id)
                # ev.dataTransfer.effectAllowed = "move"
                print("def drag_start(ev):", ev.target.id, ev.data['text'])
                # ev.stopPropagation()
                return True

            def do_drag(self, drag=True):
                # self.img.draggable = drag
                self.elt.draggable = drag
                if drag:
                    self._drag = self.drag_start
                    self._over = self.mouse_over
                    self._dover = self.drag_over
                else:
                    self._drag = self._over = lambda *_: None

            def do_drop(self, drop=False):
                if drop:
                    self._drop = self.drop
                    self._dover = self.drag_over
                else:
                    self._drop = self._dover = lambda *_: None

            @staticmethod
            def drag_over(ev):
                # ev.data.dropEffect = 'move'
                # ev.dataTransfer.dropEffect = "move"
                # ev.preventDefault()
                return False

            def drop(self, ev):
                ev.preventDefault()
                ev.stopPropagation()
                src_id = ev.data['text']
                print("def drop(self, ev):", src_id)
                # src_id = ev.dataTransfer.getData('text')

                self.drags.setdefault(src_id, lambda: None)()
                self.do_drag(False)
                return False

        return Elemento(**kwargs)


def main(jogo=None, sherlock_=sherlock):
    return Livro(jogo, sherlock_)

def spy_main():
    from _spy.vitollino.main import Jogo, STYLE
    from browser import window

    STYLE["width"], STYLE["height"] = 900, "650px"
    jogo = Jogo()
    jogo.clica_elemento = lambda *_: None
    jogo._clica_elemento = lambda _= None, j=jogo: j.clica_elemento()
    window.clica_elemento = jogo._clica_elemento
    main(jogo)


if __name__ == '__main__':
    spy_main()
