# dame.libby.main.py
from _spy.vitollino.main import Cena,Texto,Elemento
CAPITA_MARVEL = "https://www.pngkey.com/png/full/548-5482583_captain-marvel-png-clipart-carol-danvers-hulk-captain.png"
ESPACO = "https://ciencianautas.com/wp-content/uploads/2016/12/wallpapers_kate_beckinsale_planet_earth_antarctica_hd_2560x1024_interesting_places.jpg"
HOMEM_DE_FERRO = "https://cache.popcultcha.com.au/media/catalog/product/cache/1/image/1800x/040ec09b1e35df139433887a97daa66f/h/o/hotmms528d30-avengers-endgame-iron-man-mark-85-die-cast-hot-toys-action-figure-10.1554444212.jpg"
CIDADE = "http://danibrasil.com/wp-content/uploads/2015/02/paris-night.jpg"
def oi ():
    galaxia = Cena(img = ESPACO)
    paris = Cena(img = CIDADE)
    galaxia.esquerda = paris
    paris.direita = galaxia 
    danvers=Elemento(img = CAPITA_MARVEL , tit="CAROL DANVERS" , style=dict (left= 150,top=160,widht=60,height=150))
    danvers.entra(galaxia)
    faladanvers= Texto(galaxia, "Eu sou a Capita Marvel")
    faladanvers.vai()
    galaxia.vai()
    
oi()