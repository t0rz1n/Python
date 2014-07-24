#coding: utf-8

from aluno import Aluno
from docente import Docente
from random import randint

class Disciplina(object):

    _ID = 1
    limite_sala = 60
    
    def __init__(self, nome, descricao, carga, sigla, docente):
        self.id = self._ID; self.__class__._ID += 1
        self.nome = nome
        self.descricao = descricao
        self.carga = carga
        self.sigla = sigla
        self.semestre = 0
        self.docente = docente
        self._vagas = Disciplina.limite_sala
        self._alunos = {}
        self.docente.disciplina.append(self.id)
    

    @property
    def vagas(self):
        if self._vagas in range(self.limite_sala + 1):
            return self._vagas
        else:
            return 0

    def ocupar_vaga(self):
        if self.vagas:
            self._vagas -= 1
            return True
        else:
            return False

    def desocupar_vaga(self):
        if self.vagas < self.limite_sala:
            self._vagas += 1
            return True
        else:
            return False

    @property
    def matricula(self):
        return self._alunos

    @matricula.setter
    def matricula(self, alunos):
        """ 
        Recebe uma lista de alunos para serem matriculados
        ou apenas um aluno
        """
        list_matricula = []
        novos_alunos   = {}

        if isinstance(alunos, type([])):
            lista_matricula = alunos
        else:
            lista_matricula.append(alunos)
       
        for aluno in lista_matricula:
            if isinstance(aluno, Aluno):
                if self.ocupar_vaga():
                    novos_alunos.update({aluno.id: aluno})
                    aluno.disciplina.update({'id': self.id, 'media': 0})
            else:
                raise TypeError("Apenas alunos podem ser matriculados \
                                 matriculados em disciplinas")
         
        self._alunos.update(novos_alunos)
        return True

    def desmatricula(self, **kwargs):
        """
        Para cancelar a matricula de um aluno
        disciplina.desmatricula(dict_aluno) onde
        dict_aluno = {'id': [1,2,3,...], 'matricula': [1000,1001,1002,...]}
        Onde apenas um dos campos do dicionario será utilizado
        """ 
        lista_desmatricula = []        

        if kwargs.get('id') and not kwargs.get('matricula'):
            tipo_busca = 'id'
        else:
            tipo_busca = 'matricula'
       
        if not isinstance(kwargs[tipo_busca], type ([])):
            lista_desmatricula.append(kwargs[tipo_busca])
        else:
            lista_desmatricula = kwargs[tipo_busca]

        for ID, aluno in self._alunos.items():
            for ids in lista_desmatricula:
                if tipo_busca == 'id' and ID == ids:
                    del self._alunos[ID]
                    self.desocupar_vaga()
                elif tipo_busca == 'matricula' and aluno.matricula == ids:
                    del self._alunos[ID]
                    self.desocupar_vaga()



	
    def avaliar(self, alunos):
        """
        Método para avaliação de aluno
        """
        lista_alunos = []

        if not isinstance(alunos, type([])):
            lista_alunos.append(alunos)
        else:
            lista_alunos = alunos
        for aluno in lista_alunos:
            if isinstance(aluno, Aluno):
                if aluno.disciplina.get('id') == self.id:
                    nota_1 = randint(0, 100)
                    nota_2 = randint(0, 100)
                    media = (nota_1+nota_2)/2
                    aluno.disciplina.update({'media': media})









