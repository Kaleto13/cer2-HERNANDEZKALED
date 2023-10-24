from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.
class Entidades(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return (self.nombre)
    class Meta:
        verbose_name_plural = "Entidades"

class Administrador_Entidad(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pertenece_entidad = models.ForeignKey(Entidades, on_delete=models.CASCADE)


class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=20)
    detalle = models.CharField(max_length=255)
    detalle_corto = models.CharField(max_length = 126)
    tipo = [    ("S", "Suspencion de actividades"),
                ("C", "Suspencion de clases"),
                ("I", "Informacion")]
    eleccion_tipo = models.CharField(max_length=1, choices=tipo, default="I")
    fecha_publicacion = models.DateField()
    fecha_modificacion = models.DateTimeField()
    entidad = models.ForeignKey(Entidades, on_delete=models.PROTECT)
    visible = models.BooleanField(default=1)
    #poner usuario
    def __str__(self):
        datos = "Titulo: "+ self.titulo + "-" + "detalle" + self.detalle + "-" + "corto: " + self.detalle_corto + "-" + "tipo" + self.eleccion_tipo + "-" + "entidad: " 
        return datos


    
"""  
class User_manager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("No has ingresado un correo")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    nombre = models.CharField(max_length=255, blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = User_manager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = ' email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def get_full_name(self):
        return self.name
"""    