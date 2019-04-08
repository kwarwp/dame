# dame.grace.main.py
#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Sherlock
# Copyright 2010-2019 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://j.mp/GNU_GPL3>`__.
#
# Sherlock é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em `<http://www.gnu.org/licenses/>`_

"""Sherlock front end client.

.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from _spy.vitollino.main import JOGO, STYLE
STYLE.update(dict(width=900,height="700px"))
DEBUG = False


class Sherlock:
    REF = "https://i.imgur.com/{}.png"
    MAPA = {
        'A': {'N': 'aLEjWgB', 'L': 'sivjAnO', 'O': 'IZkiaDs', 'S': 'otHJhF0'},
        'B': {'N': '40K5493', 'L': 'R3bpFXD', 'O': 'dlxY8hi', 'S': 'eYM3Yp9'},
        'C': {'N': 'YJfnhy9', 'L': '94V79TA', 'O': 'Fzz2FNz', 'S': 'LFKXlB1'},
        'D': {'N': '1uWH7rU', 'L': 'b0FcjLq', 'O': '406g75C', 'S': 'HQBtUoQ'},
        'E': {'N': 'uNkTVGg', 'S': 'bculg4O', 'L': 'lUi1E1v', 'O': 'bPBT1d7'},
        'F': {'N': 'iHsggAa', 'S': 'euNeDGs', 'L': 'NqSCDQR', 'O': 'hG4mgby'},
        'G': {'N': 'XDIASJa', 'S': 'ARQZ8CX', 'L': 'pJOegNT', 'O': '9IhOYjO'},
        'H': {'N': 'WjTtZPn', 'L': 'AzvB8hs', 'O': 'SIhLGCP', 'S': 'UVnpzzE'},
        'I': {'N': 'RSdQSH1', 'S': 'UGCRJ0d', 'L': 'jSn4zsl', 'O': 'eG43vn5'},
        'J': {'N': 'MMO11Dv', 'S': 'RkWPb8Z', 'L': 'btv0qfO', 'O': 'lDezYKu'},
        'K': {'N': 'Tx9Q6vW', 'S': 'rrI94Xh', 'L': 'R6gON2E', 'O': 'Mn69uua'},
        'L': {'N': 'oAu9lkN', 'S': 'xTjd7UV', 'L': 'JMQAGvc', 'O': 'UJBMKY7'},
        'M': {'N': 'ibRxMKV', 'S': 'HtRKv7X', 'L': '1UXBodl', 'O': 'AC2KgZg'},
        'N': {'N': 'KVlUf94', 'L': 'f6vR0tY', 'O': 'GE8IsRM', 'S': 'RfUP0ez'},
        'O': {'N': 'qoHwGLW', 'S': 'OKZGVUX', 'L': 'dc2Ol59', 'O': 'I7Gn0Xx'},
        'P': {'N': 'OutDPac', 'S': 'sAIhp4b', 'L': 'nE8ti2z', 'O': '9IBwxjI'},
        'Q': {'N': 'JRYlZeN', 'S': '4BCiuYZ', 'L': 'ek4cwBg', 'O': 'vmZHZmr'},
        'R': {'N': 'qnjq624', 'S': 'nZvwdhP', 'L': 'gS4rXYk', 'O': '2Z36mLI'}
    }
    BLUEPRINT = """
..........
.ABC......
...D.E.FG.
...HIJKL..
.....M.N..
.....OPQR.
..........
    """

    def __init__(self, vit):
        class NoSalaCena:
            def __init__(self):
                self.cenas = [self] * 4
                self.meio = None

            @property
            def meio(self):
                return self

            @meio.setter
            def meio(self, *_):
                pass

            def vai(self, *_):
                pass
        nada = NoSalaCena()

        class Labirinto:
            def __init__(self, c=nada, n=nada, l=nada, s=nada, o=nada):
                self.salas = [sala_ for sala_ in [c, n, l, s, o]]
                self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
                self.lb()

            def lb(self):
                for indice, sala_ in enumerate(self.salas[1:]):
                    if not sala_:
                        return
                    self.centro.cenas[indice].meio = sala_.cenas[indice]
                    indice_oposto = (indice + 2) % 4
                    sala_.cenas[indice_oposto].meio = self.centro.cenas[indice_oposto]

        self.vit = vit
        cena = vit.cena(self.REF.format(self.MAPA['A']['N']))
        cena.vai()
        self.sala = sala_do_jogo = vit.q
        print({
            sala: {
                vento.lower(): self.REF.format(imagem) for vento, imagem in cenas.items()
            }
            for sala, cenas in self.MAPA.items()
        }) if DEBUG else 0
        self.sala_cenas = {
            sala_: {
                vento.lower(): vit.cena(self.REF.format(imagem)) for vento, imagem in cenas.items()
            }
            for sala_, cenas in self.MAPA.items()
        }
        print("self.sala_images", self.sala_cenas) if DEBUG else 0
        vit.q.c(**self.sala_cenas)
        print("sala_do_jogo.A.norte", sala_do_jogo.A, sala_do_jogo.A.norte, sala_do_jogo.A.norte.img.src)
        salas_bp = [list(linha) for linha in self.BLUEPRINT.split("\n")[1:-1]]
        linhas, colunas = len(salas_bp)-1, len(salas_bp[0])-1
        print(linhas, colunas, salas_bp) if DEBUG else 0
        print([[
                    (_posicao, _sala) for _posicao, _sala in
                    zip(
                        list("cnlso"),
                        (salas_bp[i][j], salas_bp[i-1][j], salas_bp[i][j+1], salas_bp[i+1][j], salas_bp[i][j-1])
                    )
                    if _sala != '.'
                ]for i in range(1, linhas) for j in range(1, colunas)]) if DEBUG else 0
        self.sala_do_jogo = {sala_: getattr(sala_do_jogo, sala_) for sala_ in self.MAPA.keys()}
        print("getattr", linhas, colunas, [
            {
                posicao: (sala_, self.sala_do_jogo[sala_].cenas, getattr(sala_do_jogo, sala_).nome)
                for posicao, sala_ in [
                    (_posicao, _sala) for _posicao, _sala in
                    zip(
                        list("cnlso"),
                        (salas_bp[i][j], salas_bp[i-1][j], salas_bp[i][j+1], salas_bp[i+1][j], salas_bp[i][j-1])
                    )
                    if _sala != '.'
                ]
            }
            for i in range(1, linhas) for j in range(1, colunas)
        ]) if DEBUG else 0
        blueprint = [
            Labirinto(**{
                posicao: self.sala_do_jogo[sala_] for posicao, sala_ in [
                    (_posicao, _sala) for _posicao, _sala in
                    zip(
                        list("cnlso"),
                        (salas_bp[i][j], salas_bp[i-1][j], salas_bp[i][j+1], salas_bp[i+1][j], salas_bp[i][j-1])
                    )
                    if _sala != '.'
                ]
            })
            for i in range(1, linhas) for j in range(1, colunas)
        ]
        self.blueprint = [
            {posicao: _sala for posicao in "cnlso"} for _sala in blueprint
        ]
        self.sala.A.norte.vai()


def main(bry=None):
    Sherlock(bry)


if __name__ == '__main__':
    main(JOGO)
