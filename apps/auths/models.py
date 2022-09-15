import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    """Contacts for send message"""
    email = models.EmailField(verbose_name="Почта", max_length=100)
    name = models.CharField(verbose_name="Имя", max_length=80)

    def __str__(self) -> str:
        return self.name