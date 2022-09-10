from multiprocessing import managers
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager
class DatetimeMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(AbstractBaseUser, PermissionsMixin):
    class StatusChoices(models.TextChoices):
        MECHANIC = 'Mechanic'
        ADMIN = 'Admin'
        DIRECTOR = 'Director'
        WORKER = 'Worker'

    photo = models.ImageField(upload_to='workers/', blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=64, choices=StatusChoices.choices, default=StatusChoices.WORKER)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
            
    data_joined = models.DateField(auto_now_add=True)
  
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        password = self.password
        self.set_password(password)
        super(User, self).save(*args, **kwargs)