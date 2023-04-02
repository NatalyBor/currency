# import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def save(self, *args, **kwargs):
	# 	if not self.username:
	# 		self.username = uuid.uuid4()
	#
	# 	return super().save(*args, **kwargs)
