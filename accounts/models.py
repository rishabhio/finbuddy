from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import ugettext_lazy as __
from accounts.conf import UserType


class UserManager(BaseUserManager):
    """
    manager for user model
    """

    def create_user(self, **kwargs):
        email = kwargs.get("email")
        password = kwargs.pop("password")
        email = self.normalize_email(email)
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.user_type = UserType.ADMINUSER
        user.save(using=self._db)
        return user


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(__("First Name"), max_length=32)
    last_name = models.CharField(__("Last Name"), blank=True, max_length=32)
    email = models.EmailField(__("Email"), unique=True, db_index=True)
    phone = models.CharField(__("Phone"), db_index=True, blank=True, max_length=14)
    user_type = models.PositiveSmallIntegerField(
        choices=UserType.USER_TYPES, default=UserType.WEBAPPUSER
    )
    is_staff = models.BooleanField(__("Is staff user"), default=False)
    is_app_user = models.BooleanField(__("Is Application user"), default=False)
    is_active = models.BooleanField(__("Active"), default=False)
    created_at = models.DateTimeField(__("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(__("Updated at"), auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return "{0}".format(self.first_name)

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(User, self).save(*args, **kwargs)
