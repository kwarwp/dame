# dame.anastasia.main.py
from spy.vittolino.main import Cena
LIVRO = "https://i.imgur.com/sI177hV.jpg"
PAGINA = "https://i.imgur.com/YqUFpx4.jpg"
.

class Livro:
    def __init__(self, jogo, pagina = None):
        self.livro = Cena(LIVRO)
        self.livro.vai()
        
        
if __name__ == "__main__":
    Livro()