from django.db import models

# Create your models here.

class Pessoa(models.Model):
    SEXO_CHOICES = (
        (u'F',u'Feminino'),
        (u'M',u'Masculino'),
    )


    nome = models.CharField('Nome',max_length=40)
    sobrenome = models.CharField('Sobrenome',max_length=40)
    idade = models.IntegerField('Idade')
    datanascimento = models.DateField('Data de nascimento')
    sexo = models.CharField('Sexo',max_length=4,choices=SEXO_CHOICES)

