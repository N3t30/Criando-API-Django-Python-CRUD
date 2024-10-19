
from django.db import models


# Aplicação de cadastro de usuarios
class user(models.Model):
    user_nickname = models.CharField(
        max_length=100, primary_key=True, default="")
    user_name = models.CharField(max_length=160, default="")
    user_email = models.EmailField(default=0)
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'
