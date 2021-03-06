from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import uuid


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = False

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""



    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None

    email = models.CharField(max_length=254, unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "auth_user"

class UserProfile(models.Model):

    USER_TYPE_CHOICES = (
        (0,'Zone officer'),
        (1, 'State officer'),
        (2, 'District officer'),
        (3, 'Admin'),
        (4, 'Teacher'),
        (5, 'Student')
    )


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)



    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.name

    class Meta:
        db_table = "user_profile"
