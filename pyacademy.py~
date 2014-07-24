#coding: utf-8

from academy.disciplina import Disciplina
from academy.aluno import Aluno
from academy.docente import Docente

Jao = Aluno("Jão", "04/02/1923")
Rodolfo = Aluno("Rodolfo", "06/10/1923")

Vantuil = Docente("Vantuil", "08/12/1923")

micro = Disciplina("Microprocessadores I", "Welcome to Hell", 48, "ELT005", Vantuil)

print "A disciplina %s, sigla (%s)'%s' possui %d vagas" %(micro.nome, micro.sigla, micro.descricao, micro.vagas) 

micro.matricula = [Jao, Rodolfo]
micro.avaliar([Jao, Rodolfo])


print "%s nota: %d" %(Jao.nome, Jao.disciplina['media'])

"""
print "A disciplina %s, sigla (%s)'%s' possui %d vagas" %(micro.nome, micro.sigla, micro.descricao, micro.vagas) 

micro.desmatricula(id = [Jao.id,Rodolfo.id])
print "A disciplina %s, sigla (%s)'%s' possui %d vagas" %(micro.nome, micro.sigla, micro.descricao, micro.vagas)

print "O professor é: %s" %micro.docente.nome
"""

