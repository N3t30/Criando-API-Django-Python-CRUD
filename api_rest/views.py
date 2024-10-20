import json

from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def get_users(request):
    # VERIFICAÇÃO CASO O ACESSO AO NAVEGADOR NÃO SEJA GET
    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_nick(request, nick):

    try:
        user = User.objects.get(pk=nick)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = UserSerializer(user)
        return Response(serializer.data)

# CRUDZÃO DA MASSA


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['user']:

                user_nickname = request.GET['user']
                try:
                    user = User.objects.get(pk=user_nickname)
                except User.DoesNotExist:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# CRIANDO DADO
    if request.method == 'POST':
        new_user = request.data

        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

# EDITANDO DADOS  PUT
    if request.method == 'PUT':

        nickname = request.data['user_nickname']
        try:
            update_user = user.objects.get(pk=nickname)
        except User.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)
        print(request.data)

        serializer = UserSerializer(update_user, data=request.data)

        if serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_202_ACCEPTED0)


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
