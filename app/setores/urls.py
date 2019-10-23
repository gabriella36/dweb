from django.urls import include, path
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views as setores

app_name = 'setores'

urlpatterns = [
	# admin
	path('dashboard/', setores.Dashboard.as_view(), name='dashboard'),
	path('solicitacoes/informatica/', setores.Info.as_view(), name='informatica'),
	path('solicitacoes/administracao/', setores.Adm.as_view(), name='adm'),
	path('solicitacoes/cozinha/', setores.Coz.as_view(), name='coz'),
	path('solicitacoes/limpeza/', setores.Lim.as_view(), name='lim'),
	# user - solicitar
	path('solicitar/informatica/', setores.SInfo.as_view(), name='s-info'),
	path('solicitar/administracao/', setores.SAdm.as_view(), name='s-adm'),
	path('solicitar/cozinha/', setores.SCoz.as_view(), name='s-coz'),
	path('solicitar/limpeza/', setores.SLim.as_view(), name='s-lim'),
	# user - visualizar solicitações
	path('minhas/solicitacoes/informatica/', setores.UserInfo.as_view(), name='user-info'),
	path('minhas/solicitacoes/administracao/', setores.UserAdm.as_view(), name='user-adm'),
	path('minhas/solicitacoes/cozinha/', setores.UserCoz.as_view(), name='user-coz'),
	path('minhas/solicitacoes/limpeza/', setores.UserLim.as_view(), name='user-lim'),
]