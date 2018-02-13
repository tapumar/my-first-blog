from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^sobre$', views.sobre, name='sobre' ),
    url(r'^login/sobre$', views.sobre, name='login_sobre' ),
    url(r'^contatos', views.contatos, name='contatos' ),
    url(r'^login/contatos', views.contatos, name='login_contatos' ),
    url(r'^servicos', views.servicos_list, name='servicos_list'),
    url(r'^login/servicos', views.servicos_list, name='login_servicos_list'),
    url(r'^amigos', views.amigos, name='amigos'),
    url(r'^login/amigos', views.amigos, name='amigos'),
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

]
