#coding: utf-8

from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class Semestre(object):

    _ID = 1
    
    def _semestre_nome(self, datetime):
        ''' Denomina o nome do Semestre, sendo o primeiro
        do ano ímpar, e o segundo par
        '''

        mes = datetime.month

        if mes < 6:
            res = '1'
        else:
            res = '2'


    def __init__(self):
        self.id = self._ID; self.__class__._ID += 1
        self.nome = "Semestre" +
                     str(date.today().year) + "/" +
                     self._semestre_nome(datetime)
        self.alunos = []
        self.disciplinas = []
        self.data_inicio = datetime.today()
        self.data_final  = self.data_inicio + relativedelta(months=6)
