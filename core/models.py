from django.db import models


# Create your models here.
'''
Não Funciona
Erro:
new_class = super_new(cls, name, bases, new_attrs)
TypeError: Cannot create a consistent method resolution
order (MRO) for bases Nivel, Model

class Nivel(models.Model):
    basico = 'Basico'
    medio = 'Intermediário'
    avancado = 'Avançado'
    nivel_opc = (
        (basico, 'Basico'),
        (medio, 'Intermediário'),
        (avancado, 'Avançado')
    )
    nivel = models.CharField(
        max_length=13,
        choices = nivel_opc
        )
    def __init__(self, nivel):
        self.nivel = nivel

    def __str__(self):
       return self.nivel in (self.nivel_opc)    
'''

class Linguagens(models.Model):    
    nome = models.CharField(max_length=80)
    '''
    basico = 'Basico'
    medio = 'Intermediário'
    avancado = 'Avançado'
    nivel_opc = (
        (basico, 'Basico'),
        (medio, 'Intermediário'),
        (avancado, 'Avançado')
    )
    nivel = models.CharField(
        max_length=13,
        choices = nivel_opc,
        default = basico,
        )
   '''
    def __str__(self):
        return self.nome

class Frameworks(models.Model):    
    nome = models.CharField(max_length=80)
    '''
    basico = 'Basico'
    medio = 'Intermediário'
    avancado = 'Avançado'
    nivel_opc = (
        (basico, 'Basico'),
        (medio, 'Intermediário'),
        (avancado, 'Avançado')
    )
    nivel = models.CharField(
        max_length=13,
        choices = nivel_opc,
        blank = True
        )
    '''    
    def __str__(self):
        
        return  self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    mensagem = models.CharField(max_length=501)

    def __str__(self):
        return  self.nome, self.email, self.mensagem




