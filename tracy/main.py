# dame.tracy.main.py
from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
PRAIA="https://img.freepik.com/fotos-gratis/bela-praia-tropical-e-mar-com-coqueiro-na-ilha-paradisiaca_74190-2206.jpg?size=626&ext=jpg"
RYU="https://http2.mlstatic.com/kit-display-street-fighter-c-8-pecas-painel-20-x-150-mt-D_NQ_NP_679648-MLB31207888566_062019-F.jpg"
class arroz():
    praia=Cena(img=PRAIA)
    ryu=Elemento(img=RYU)
    ryu.entra(praia)
    praia.vai()
arroz()    