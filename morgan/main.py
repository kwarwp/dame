from _ spy.vitollino.main import Cena , Texto , Elemento
from _ spy.vitollino.main import Inventario as inv
PAISAGEM = "https://pngimage.net/wp-content/uploads/2018/06/fundo-paisagem-png.png/"
THOR = "https://pngmafia.net/image/2019/01/Thor-10-min.png"
CAMPO = "https://png.pngtree.com/element_origin_min_pic/16/09/08/2157d1695243d31.jpg"
TIANA = "http://www.stickpng.com/assets/images/5a96849c9fc609199d0fefaa.png"
def funcoes ( ):
    Paisagem = Cena (img =PAISAGEM)
    Campo = Cena (img =CAMPO)
    Campo.direita = Paisagem
    Paisagem.esquerda = Campo
    Thor = Elemento (img =THOR,tit= "Capitão",style =dict (left=150,top=160,width=60,height=200))
    Thor.entra(Paisagem)
    eThor=Texto(Paisagem,"Olá, vim de Asgard e caí nessa praia. Sou Thor, Deus do Trovão e filho de Odin")
    Thor=eThor.vai
    Tiana = Elemento (img =TIANA,tit= "Tiana",style=dict(left=150,top=160,width=60,height=200))
    Tiana.entra(Campo)
    eTiana=Texto(Campo,"Oi, me chamo Tiana e estou a procura do meu príncipe encantado.Você pode me ajudar?")
    Tiana=eTiana.vai()
    
    Campo.vai()
funcoes()