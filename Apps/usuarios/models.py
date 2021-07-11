from django.db import models

# Create your models here.

class UsuarioManager():
    def _crear_usuario(self, rut,usuario, correo, nombre, apellido, contrasena):
        user = self.model(
            rut = rut,
            usuario = usuario,
            correo = correo,
            nombre = nombre,
            apellido = apellido
        )
        user.set_password(contrasena)
        user.save(using = self.db)

        return user

    def create(self, rut, usuario, correo, nombre, apellido, contrasena):
        return self._crear_usuario(rut, usuario, correo, nombre, apellido, contrasena)

class Usuario():
    rut = models.IntegerField()
    usuario = models.CharField(max_length=200 , unique=True)
    correo = models.EmailField('Correo Electrónico', max_length=200, unique=True)
    nombre = models.CharField('Nombre', max_length=200, blank=True , null=True)
    apellido = models.CharField('Apellido', max_length=200, blank=True, null=True)
    objects = UsuarioManager()

    CAMPO_USUARIO = 'usuario'
    REQUIRED_FIELDS = ['usuario','rut','correo','nombre','apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'