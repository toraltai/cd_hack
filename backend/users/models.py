from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, password=None, **extra):

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email),
                          full_name=full_name, phone_number=phone_number, **extra)

        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra):
        if password is None:
            raise TypeError('Superusers must have a password.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, verbose_name='ФИО', null=True)
    phone_number = models.CharField(max_length=15, default='+996', null=True)
    is_active = models.BooleanField(default=True)
    username = None
    is_staff = models.BooleanField(default=False)
    code = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return f'{self.id}. {self.email}'
    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor', editable=False)

    def __str__(self):
        return f'{self.id}. {self.user.full_name}'