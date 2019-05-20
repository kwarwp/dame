# dame.stacy.main.py
from _spy.vitollino.main import Cena , Texto , Elemento
from _spy.vitolli.main import inventario as inv
Bart_Simpson = "https://www.multarte.com.br/wp-content/uploads/2019/03/bart-simpson-hypebeast-3.png"
Mar = "https://r-ec.bstatic.com/images/hotel/max1024x768/650/65026569.jpg"
Furia_da_Noite = "https://i.pinimg.com/originals/1e/45/c7/1e45c7fd135d3b8fed8f18a33447a019.png"
Vulcao = "https://mundoeducacao.bol.uol.com.br/upload/conteudo_legenda/aed822dbf3f1a9eaf83218845b978bf7.jpg"
def oi ():
    mar = Cena(img = Mar)
    vulcao = Cena (img = Vulcao)
    mar_esquerda = Vulcao
    vulcao.direita = Mar
    bart_Simpson = Elemento (img = Bart_Simpson, tit="Oi, eu sou o Bart!", style = dict(left= 150, top=60, width=60, height=200))
    bart_Simpson.entra(mar)
    falaBart=Texto(mar,"E aí, estamos nas Ilhas Maldivas! Nem sei como consegui parar aqui.")
    furia_da_Noite = Elemento (img = Furia_da_Noite, tit="Olá, sou o Furia da Noite", style = dict(left= 150, top=60, width=60, height=200))
    furia_da_Noite.entra(vulcao)
    falaFuria=Texto(vulcao,"Estou animado pra poder sobrevoar e ver o que acontece lá dentro!")
    mar.vai()
    falaBart.vai()
oi()
