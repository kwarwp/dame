
{'date': 'Mon May 20 2019 10:23:32.544 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 13
  Bart_Simpson = Elemento (img = Bart Simpson, tit"Oi, eu sou o Bart!", Style = dict(left=150, top=60, weith=60, heith=200))
                                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon May 20 2019 10:24:47.212 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 13
  bart_Simpson = Elemento (img = Bart_Simpson, tit"Oi, eu sou o Bart!", Style = dict(left=150, top=60, weith=60, heith=200))
                                                   ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon May 20 2019 10:27:34.682 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 16
  Furia_da_Noite = Elemento (img = Furia da Noite, tit"Olá, sou o Furia da Noite", Style = dict(left=150, top=60, weith=60, heith=200))
                                          ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon May 20 2019 10:29:05.57 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 16
  furia_da_Noite = Elemento (img = Furia da Noite, tit="Olá, sou o Furia da Noite", Style = dict(left=150, top=60, width=60, height=200))
                                          ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon May 20 2019 10:29:43.463 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 6
    Furia.da.Noite = "https://i.pinimg.com/originals/1e/45/c7/1e45c7fd135d3b8fed8f18a33447a019.png"
NameError: name 'Furia' is not defined
'''},