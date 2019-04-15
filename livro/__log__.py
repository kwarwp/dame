
{'date': 'Mon Apr 15 2019 12:12:33.568 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''sala_do_jogo.A.norte <_spy.vitollino.main.Sala object> <_spy.vitollino.main.Cena object> https://i.imgur.com/aLEjWgB.png
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 362
    spy_main()
  module <module> line 358
    main(jogo)
  module <module> line 347
    return Livro(jogo, sherlock_)
  module <module> line 119
    cromo.chave_cromossomo(cena=self.jogo.sala.A.norte)
  module <module> line 198
    chave = self.livro.cria_arrastante(cena=self.jogo.i,
  module <module> line 343
    return Elemento(**kwargs)
  module <module> line 244
    self.style.update(inv_style if (cena == self.jogo.i) else {})
AttributeError: 'Elemento' object has no attribute 'jogo'
'''},
{'date': 'Mon Apr 15 2019 13:26:22.566 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 201
  self.livro.cria_arrastante(
                                                                                  ^
SyntaxError: invalid syntax
'''},