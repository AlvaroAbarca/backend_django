from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account(AbstractUser):

    class Meta:
        verbose_name = ("Account")
        verbose_name_plural = ("Accounts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Account_detail", kwargs={"pk": self.pk})
