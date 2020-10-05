from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Vegetarian(models.Model):
    v_type = models.CharField(max_length=50)
    

class Allergy(models.Model):
    a_type = models.TextField()


class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None):
        if not email :
            raise ValueError('must have user email')
        user = self.model(
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password ):

        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    allergy = models.ManyToManyField(
        Allergy,
        blank=True,
        related_name = 'Allergy',
    )
    vegetarian = models.ForeignKey(
        Vegetarian,
        on_delete=models.CASCADE,
        blank=True, null=True
        )

    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
