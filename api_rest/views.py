import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import user
from .serializers import UserSerializer


@api_view(['GET'])
def get_users(request):
    # VERIFICAÇÃO CASO O ACESSO AO NAVEGADOR NÃO SEJA GET
    if request.method == 'GET':
        users = user.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


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
