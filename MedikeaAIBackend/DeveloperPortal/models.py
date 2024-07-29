from datetime import datetime, timedelta
from django.db import models
from Main_app.utils import *
from Main_app.models import * # type: ignore
from uuid import uuid4


class Developer(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'developers'
        verbose_name = 'Developer'
        verbose_name_plural = 'Developers'
        ordering = ['full_name']

class UserApi(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid4)
    username = models.CharField(max_length=255)
    client_id = models.CharField(max_length=255. null=True, blank=True)
    api_key = models.CharField(max_length=255. null=True, blank=True)
    api_key_expiration = models.DateTimeField(null=True, blank=True)
    is_live = models.BooleanField(default=False)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username + self.developer.full_name
    
    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = generating_api_key()
            self.api_key_expiration = datetime.now() + timedelta(days=30*366*2)
        super().save(*args, **kwargs)
    

    def is_expired(self):
        return self.api_key_expiration < datetime.now()
    
    class Meta:
        db_table = 'users_api'
        verbose_name = 'User API'
        verbose_name_plural = 'Users API'
        ordering = ['username']


