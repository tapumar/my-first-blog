from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$', views.sobre),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^sobre$', views.sobre, name='sobre' ),
    url(r'^contatos', views.contatos, name='contatos' ),
    url(r'^servicos', views.servicos_list, name='servicos_list'),
    url(r'^amigos', views.amigos, name='amigos'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^encanador', views.encanadores, name='encanador'),
    url(r'^eletricista', views.eletricistas, name='eletricista'),
    url(r'^pedreiro', views.pedreiros, name='pedreiro'),
    url(r'^costura', views.costura, name='costura'),
    url(r'^manicure', views.manicures, name='manicure'),
    url(r'^cabelo', views.cabelo, name='cabelo'),
    url(r'^jardinagem', views.jardinagem, name='jardinagem'),
    url(r'^cadastro', views.Criar.as_view(), name='cadastro'),
    url(r'^lista', views.Lista.as_view(), name='lista'),

]
