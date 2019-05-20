
{'date': 'Mon May 20 2019 10:27:14.24 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 12
  THOR = Elemento (img =Thor,tit "Capitão",Style =dict (left=150,top=160,width=60,height=200))
                                  ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon May 20 2019 10:28:40.545 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 16
  Tiana = Elemento (img =Tiana,tit "Tiana",Style=dict(left=150,top=160,width=60,height=200))
                                    ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon May 20 2019 10:30:23.26 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 22
    funcoes()
  module <module> line 12
    THOR = Elemento (img =THOR,tit= "Capitão",Style =dict (left=150,top=160,width=60,height=200))
UnboundLocalError: local variable 'THOR' referenced before assignment
'''},