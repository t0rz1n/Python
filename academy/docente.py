#coding: utf-8

from pessoa import Pessoa

class Docente(Pessoa):

    _ID = 1

    def __init__(self, nome, nascimento)
        Pessoa.__init__(self, nome, nascimento, "docente")
        self.id = self._ID; self.__class__._ID += 1
        self.disciplina = []
