# dame.roxanne.main.py
from _spy.vitollino.main import Cena,Texto,Elemento
from _spy.vitolli.main import invetario as inv
HOMEM_DE_FERRO = "https://3.bp.blogspot.com/-KeRoySaYA8w/V1IMHgntcoI/AAAAAAAAEEA/ytk2oRoCQtc3vSiuFTLK5OFwLeLWAGG-gCLcB/s1600/homemdfet.png"
CAMPO = "http://imagensemoldes.com.br/wp-content/uploads/2018/06/Futebol-Campo-de-Futebol-2-PNG.png"
CAPITAO_AMERICA = "https://2.bp.blogspot.com/-gL72SZb5r1A/V5zitzG0yiI/AAAAAAAAH1M/glC6e03Cx6E8k6qXLg61SB3r06xcfoTfACLcB/s1600/captain_america_by_cptcommunist-da55g3v.png"
PLANETA = "https://images.vexels.com/media/users/3/152418/isolated/preview/098366e6994dd75ab46b47cd27b2c9d4---cone-do-planeta-terra-by-vexels.png"
def oi ():
    jogo = Cena(img = CAMPO)
    terra = Cena(img = PLANETA)
    jogo.esquerda = PLANETA
    terra.direita = PLANETA
    tony=Elemento(img = HOMEM_DE_FERRO , tit="TONY STARK" , style=dict (left= 150,top=160,width=60,height=200))
    tony.entra(paisagem)
    falatony= Texto(paisagem, ("Eu sou o homem de ferro"))
    tony = falatony.vai
    