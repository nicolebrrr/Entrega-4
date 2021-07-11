from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Apps.usuarios.models import Usuario
from Apps.usuarios.api.serializer import UsuarioSerializer, UsuarioListSerializer

@api_view(['GET','POST'])
def user_api_view(request):

    # list
    if request.method == 'GET':
        # queryset
        users = Usuario.objects.all()
        users_serializer = UsuarioListSerializer(users,many = True)
#        return Response(users_serializer.data,status = status.HTTP_200_OK)
        return JsonResponse(list(users.values()),safe=False)    
    # create
    elif request.method == 'POST':
        user_serializer = UsuarioSerializer(data = request.data)
        
        # validation
        if user_serializer.is_valid():
            user_serializer.save()            
            return Response({'message':'Usuario creado correctamente!'},status = status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk=None):
    # queryset
    user = Usuario.objects.filter(id = pk).first()

    # validation
    if user:

        # retrieve
        if request.method == 'GET': 
            Usuario_serializer = UsuarioSerializer(Usuario)
            return Response(Usuario_serializer.data,status = status.HTTP_200_OK)
        
        # update
        elif request.method == 'PUT':
            user_serializer = UsuarioSerializer(Usuario,data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)
            return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        # delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario Eliminado correctamente!'},status = status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un usuario con estos datos'},status = status.HTTP_400_BAD_REQUEST)