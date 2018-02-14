from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

servicos_choice = (
("Encanador" , "Encanador"),
("Manicure", "Manicure"),
("Pedreiro", "Pedreiro"),
("Cabelo", "Cabelo"),
("Costura", "Costura"),
("Eletricista", "Eletricista"),
("Jardinagem", "Jardinagem"),
("Outros","Outros")
)
class Inscricao(models.Model):
        servico = models.CharField(choices=servicos_choice, max_length=100)
        nome = models.CharField(max_length=100)
        cpf = models.CharField('CPF', max_length=11, unique=True)
        idade = models.IntegerField()
        email = models.EmailField(unique=True)
        telefone = models.CharField(max_length=20, blank=True)

        class Meta:
                ordering = ['nome']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __unicode__(self):
                return self.nome
