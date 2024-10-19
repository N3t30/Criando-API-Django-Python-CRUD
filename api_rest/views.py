import json

from django.shortcuts import HttpResponse, JsonResponse, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import user
from .serializers import UserSerializer

# #  Resumo de banco de dados, alguns comandos mais usados
# def databaseEmdjango():

#     data = user.objects.get(pk='user_nickname') #OBJETO
#     # Busca um objeto único no banco de dados
#     data = user.objects.filter(user_age='25')  # QUERYSET
#     # Retorna uma lista de objetos que você tem critério de filtro
#     data = user.objects.exclude(USER_AGE='25')  # QUERYSET
#     # Retorna uma lista de objetos, excluindo aqueles
#     data.save()
#     #Salva o objeto atualno banco de dados
#     data.delete()
#     # Apagar o objeto atual do banco de dados
