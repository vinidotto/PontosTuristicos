from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuarios =  models.ForeignKey(User, on_delete = models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add = True)
    status = models.BooleanField(default=True)


    def __str__(self) :
        return self.usuarios.first_name