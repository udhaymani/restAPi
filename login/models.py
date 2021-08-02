from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
 # baseuser manager
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    '''Manager for User Profiles'''
    #creates the user as such the user created by django admin by default
    def create_user(self,email,name,passwd=None):
        
        if not email:
            raise ValueError('users must have Email address')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        
        # the reason behind setting password is that the password will never saved as plain text once the user enters the password into the login page

        user.set_password(passwd)
        #inorder to support multiple databases we need to specify this self._db
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        '''creates & saves the new super user'''

        user = self.create_user(email,name,password)

        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user



        


# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    '''Database models for UserProfile'''
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''retrives full name of user'''
        return self.name

    def get_short_name(self):
        '''retrives short name of user'''
        return self.name

    def __str__(self):
        '''return string representation of user'''
        return self.email



    