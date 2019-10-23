from django.db import models
from app.core.models import UUIDUser

class Informatica(models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, verbose_name = 'Usuário', related_name = 'users')
	sala = models.CharField(max_length = 255, verbose_name = 'Sala')
	horario = models.TimeField(verbose_name = 'Horário')
	responsavel = models.CharField(max_length = 255, verbose_name = 'Responsável')
	data_solicitacao = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return "Solicitação Nº %i" % self.id

class Limpeza(models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, verbose_name = 'Usuário', related_name = 'user')
	local = models.CharField(max_length = 255, verbose_name = 'Local da Limpeza')
	incidente = models.TextField(verbose_name = 'Descrição do Incidente')
	data_solicitacao = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return "Solicitação Nº %i" % self.id

class Cozinha(models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, verbose_name = 'Usuário', related_name = 'usuarios')
	descricao = models.TextField(verbose_name = 'Descrição da Refeição')
	data_solicitacao = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return "Solicitação Nº %i" % self.id

class Administracao(models.Model):
	usuario = models.ForeignKey(UUIDUser, on_delete = models.CASCADE, verbose_name = 'Usuário', related_name = 'usuario')
	motivo = models.TextField(verbose_name = 'Motivo da Reunião')
	data = models.DateField(verbose_name = 'Data')
	hora = models.TimeField(verbose_name = 'Horário')
	data_solicitacao = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return "Reunião Nº %i" % self.id

