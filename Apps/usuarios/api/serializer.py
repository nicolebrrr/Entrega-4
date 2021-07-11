from rest_framework import serializers
from Apps.usuarios.models import Usuario

class UsuarioTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('rut','usuario', 'correo', 'nombre', 'apellido', 'contrasena')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
    def create(self,validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['contrasena'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        updated_user = super().update(instance,validated_data)
        updated_user.set_password(validated_data['contrasena'])
        updated_user.save()
        return updated_user

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario

    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'usuario': instance['usuario'],
            'correo': instance['correo'],
            'contrasena': instance['contrasena']
        }