
{'date': 'Tue May 21 2019 11:13:39.732 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
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
  module <module> line 4
    main()
  module livro.main line 350
    return Livro(jogo, sherlock_)
  module livro.main line 110
    self.texto_da_pagina_do_livro = self.jogo.codigo(
AttributeError: 'NoneType' object has no attribute 'codigo'
'''},