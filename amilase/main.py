# dame.amilase.main.py
from elemento.main import Elemento
from _spy.vitollino.main import INVENTARIO as inv
AMILASE = "https://i.imgur.com/6sPzHr4.png"
COLA = "https://i.imgur.com/fUmF8X9.png"


class Amilase:
    def __init__(self, vit):
        self.vit = vit
        self.porta = vit.sala.C.sul
        self.amilase = Elemento(AMILASE, tit="Amilase Sintética", drag=True)
        self.cola = Elemento(COLA, tit="Cola Glicosada", drop={"Amilase Sintética": self.abre}, 
        cena=self.porta, x=375, y=300, w=75, h=100, style={"opacity": 0.5})
        inv.bota(self.amilase)
        
    def abre(self, *_):
        self.porta.meio =  self.vit.sala.D.sul       
