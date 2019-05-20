# dame.adda.main.py
from _spy. vitollino.main import Cena, Texto, Elemento
from _spy. vitolli.main import inventorio as inv
FLORESTA= 'https://wcrates.files.wordpress.com/2015/07/woods-landscape-wallpaper.jpg'
RIO= 'https://www.settemuse.it/sfondi_ambiente/natura_selvaggia/natura_selvaggia_003.jpg'
BATMAN= 'http://www.pngonly.com/wp-content/uploads/2017/06/Batman-Cartoon-PNG-Image-01.png'
PINGUIM= 'https://i.pinimg.com/originals/e2/74/aa/e274aa71319d9e08bd51840ef74175d7.jpg'
def juntarimagem():
    verde = Cena(img = FLORESTA)
    agua = Cena(img = RIO)
    verde.direita = agua
    agua.esquerda= verde
    morcego=Elemento(img = BATMAN , tit="BATMAN", style=dict (left=150,top=160,width=60,height=200))
    morcego.entra (verde)
    falamorcego= Texto(verde, "eu vou te pegar pinguim")
    falamorcego.vai()
    feio = Elemento (img = PINGUIM , tit = "PINGUIM", style=dict (left=150,top=160,width=60,height=200))
    feio.entra (agua)
    falafeio= Texto(agua, "impossivel")
    falafeio.vai()
    verde.vai()
    agua.vai()
juntarimagem()