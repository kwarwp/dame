# dame.anastasia.main.py
from _spy.vitollino.main import Cena, Codigo, STYLE
STYLE["width"] = 900
STYLE["height"] = "650px"
LIVRO = "https://i.imgur.com/sI177hV.jpg"
PAGINA = "https://i.imgur.com/YqUFpx4.jpg"

TEXTO = """<div style="width:100%; text-align: center;">
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
    """

class Dna:
    def __init__(self, jogo=None, pagina = None):
        self.livro = Cena(LIVRO)
        self.texto_da_pagina_do_livro = Codigo(
            codigo="", topo=TEXTO,
            style=dict(left=440, top=20, width=380))
        self.texto_da_pagina_do_livro.entra(self.livro)
        self.livro.vai()
        
        
if __name__ == "__main__":
    Dna()