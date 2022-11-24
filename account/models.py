from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    """ MyAccountManager"""
    def create_user(self, first_name,last_name, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a username')

        user=self.model(
            email=self.normalize_email(email), # normalize, makes the email into lowercase
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password):
        """
        Creates and saves a superuser with the given email, password.
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email), # normalize, makes the email into lowercas,
            password=password,
        )

        user.is_admin = True
        user.is_super_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    """Account Class for user"""
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    #required fields
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_active= models.BooleanField(default=False)
    is_super_admin= models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username', 'first_name', 'last_name']

    objects=MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    