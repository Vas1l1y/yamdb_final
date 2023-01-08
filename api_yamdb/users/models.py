"""Database settings of the 'Users' application."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Modified model User."""

    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLE_OPTIONS = [
        (USER, "user"),
        (MODERATOR, "moderator"),
        (ADMIN, "admin"),
    ]
    role = models.CharField(
        "Role", max_length=20, choices=ROLE_OPTIONS, default=USER
    )
    email = models.EmailField(unique=True)
    bio = models.TextField("Biography", blank=True)

    class Meta:
        ordering = ("username",)
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_staff or self.is_superuser
