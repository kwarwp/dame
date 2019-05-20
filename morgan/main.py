from _ spy.vitollino.main import Cena , Texto , Elemento
from _ spy.vitollino.main import Inventario as inv
PAISAGEM = "https://pngimage.net/wp-content/uploads/2018/06/fundo-paisagem-png.png/"
THOR = "https://pngmafia.net/image/2019/01/Thor-10-min.png"
CAMPO = "https://png.pngtree.com/element_origin_min_pic/16/09/08/2157d1695243d31.jpg"
TIANA = "https://www.pngkit.com/png/detail/168-1689175_princess-tiana-roommates-disney-princess-the-frog-princess.png"
def funcoes ( ):
    Paisagem = Cena (img =Paisagem)
    Campo = Cena (img =Campo)
    Campo.direita = Paisagem
    Paisagem.esquerda = Campo
    THOR = Elemento (img =Thor,tit "Capitão",Style =dict (left=150,top=160,width=60,height=200))
    Thor.entra(Paisagem)
    eThor=Texto(Paisagem,"Olá, vim de Asgard e caí nessa praia. Sou Thor, Deus do Trovão e filho de Odin")
    Thor=eThor.vai
    Tiana = Elemento (img =Tiana,tit "Tiana",Style=dict(left=150,top=160,width=60,height=200))
    Tiana.entra(Campo)
    eTiana=Texto(Campo,"Oi, me chamo Tiana e estou a procura do meu príncipe encantado.Você pode me ajudar?")
    Tiana=eTiana.vai
    
    Campo.vai()
    funcoes()
    