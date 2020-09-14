from django.db import models



# Create your models here.
class Lembrete(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length = 30)
    mensagem = models.CharField(max_length = 200)
    def __str__(self):
        return (self.id)

