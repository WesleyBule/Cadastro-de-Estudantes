from django.db import models

class Estudantes(models.Model):
    nome = models.CharField(verbose_name="nome" ,max_length=120 ,blank=False , null=False)
    idade = models.IntegerField(verbose_name="idade" ,blank=False, null=False)
    turma = models.CharField(verbose_name="turma" ,blank=False, null=False)