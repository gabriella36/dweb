from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from .models import *
from app.core.models import UUIDUser

class Dashboard(View):
	def get(self, request):
		if request.user.is_staff:
			informatica = Informatica.objects.all()
			cozinha = Cozinha.objects.all()
			administracao = Administracao.objects.all()
			limpeza = Limpeza.objects.all()
			return render(request, 'core/dashboard.html', {'informatica': informatica, 'cozinha': cozinha, 'administracao': administracao, 'limpeza': limpeza})
		informatica = Informatica.objects.filter(usuario = self.request.user.pk)
		cozinha = Cozinha.objects.filter(usuario = self.request.user.pk)
		administracao = Administracao.objects.filter(usuario = self.request.user.pk)
		limpeza = Limpeza.objects.filter(usuario = self.request.user.pk)
		return render(request, 'core/dashboard.html', {'informatica': informatica, 'cozinha': cozinha, 'administracao': administracao, 'limpeza': limpeza})

# ADMINISTRADOR - INICIO
class Info(ListView):
	model = Informatica
	template_name = 'setores/admin/solicitacoes-info.html'
	def get_context_data(self, **kwargs):
		kwargs['object_list'] = Informatica.objects.all().order_by('-data_solicitacao')
		return super(Info, self).get_context_data(**kwargs)

class Adm(ListView):
	model = Administracao
	template_name = 'setores/admin/solicitacoes-adm.html'
	def get_context_data(self, **kwargs):
		kwargs['object_list'] = Administracao.objects.all().order_by('-data_solicitacao')
		return super(Adm, self).get_context_data(**kwargs)

class Coz(ListView):
	model = Cozinha
	template_name = 'setores/admin/solicitacoes-coz.html'
	def get_context_data(self, **kwargs):
		kwargs['object_list'] = Cozinha.objects.all().order_by('-data_solicitacao')
		return super(Coz, self).get_context_data(**kwargs)

class Lim(ListView):
	model = Limpeza
	template_name = 'setores/admin/solicitacoes-lim.html'
	def get_context_data(self, **kwargs):
		kwargs['object_list'] = Limpeza.objects.all().order_by('-data_solicitacao')
		return super(Lim, self).get_context_data(**kwargs)
# ADMINISTRADOR - FIM

# USUARIO - INICIO
class SInfo(View):
	def get(self, request):
		return render(request, 'setores/user/solicitar/info.html')

	def post(self, request):
		info = Informatica(usuario = self.request.user, sala = request.POST.get('sala'), horario = request.POST.get('hora'), responsavel = request.POST.get('res'))
		info.save()
		return redirect('setores:dashboard')

class SLim(View):
	def get(self, request):
		return render(request, 'setores/user/solicitar/lim.html')

	def post(self, request):
		lim = Limpeza(usuario = self.request.user, local = request.POST.get('local'), incidente = request.POST.get('incidente'))
		lim.save()
		return redirect('setores:dashboard')

class SCoz(View):
	def get(self, request):
		return render(request, 'setores/user/solicitar/coz.html')

	def post(self, request):
		coz = Cozinha(usuario = self.request.user, descricao = request.POST.get('desc'))
		coz.save()
		return redirect('setores:dashboard')

class SAdm(View):
	def get(self, request):
		return render(request, 'setores/user/solicitar/adm.html')

	def post(self, request):
		adm = Administracao(usuario = self.request.user, motivo = request.POST.get('motivo'), data = request.POST.get('data'), hora = request.POST.get('hora'))
		adm.save()
		return redirect('setores:dashboard')

class UserInfo(ListView):
	model = Informatica
	template_name = 'setores/user/minhas/solicitacoes-info.html'
	def get_context_data(self, **kwargs):
		kwargs['object_list'] = Informatica.objects.filter(usuario = self.request.user.pk).order_by('-data_solicitacao')
		return super(UserInfo, self).get_context_data(**kwargs)

class UserAdm(ListView):
	model = Administracao
	template_name = 'setores/user/minhas/solicitacoes-adm.html'
	def get_context_data(self, **kwargs):
		kwargs['object_list'] = Administracao.objects.filter(usuario = self.request.user.pk).order_by('-data_solicitacao')
		return super(UserAdm, self).get_context_data(**kwargs)

class UserCoz(ListView):
	model = Cozinha
	template_name = 'setores/user/minhas/solicitacoes-coz.html'
	def get_context_data(self, **kwargs):
		kwargs['object_list'] = Cozinha.objects.filter(usuario = self.request.user.pk).order_by('-data_solicitacao')
		return super(UserCoz, self).get_context_data(**kwargs)

class UserLim(ListView):
	model = Limpeza
	template_name = 'setores/user/minhas/solicitacoes-lim.html'
	def get_context_data(self, **kwargs):
		kwargs['object_list'] = Limpeza.objects.filter(usuario = self.request.user.pk).order_by('-data_solicitacao')
		return super(UserLim, self).get_context_data(**kwargs)
# USUARIO - FIM
