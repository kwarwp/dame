# dame.danae.main.py
from grace.main import main as grace


class Livro:
    def __init__(self, casa):
        livro_fechado = "https://i.imgur.com/ty2fWuE.gif"
        livro_aberto = "https://i.imgur.com/sI177hV.jpg"
        self.casa = casa()


def main(bry=grace):
    return Livro(bry)


if __name__ == '__main__':
    main(grace)
