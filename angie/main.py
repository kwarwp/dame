# dame.angie.main.py
from _spy.vitollino.main import Cena
from _spy.vitollino.main import STYLE
STYLE["width"] = 900
STYLE["height"] = 700
CENALIVRO = "https://i.imgur.com/sI177hV.jpg"

class Livro:
    def __init__(self):
        self.livro = Cena(img=CENALIVRO)
        self.livro.vai()
        
        
if __name__ == "__main__":
    Livro()
        
        
        
    
