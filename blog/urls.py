from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^sobre$', views.sobre, name='sobre' ),
    url(r'^contatos', views.contatos, name='contatos' ),
    url(r'^servicos', views.servicos_list, name='servicos_list'),
    url(r'^amigos', views.amigos, name='amigos'),
]
