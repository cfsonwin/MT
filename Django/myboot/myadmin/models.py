from django.db import models
from datetime import datetime


# Create your models here.

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=100, unique=True)
    u_name = models.CharField(max_length=30, default='user')
    u_password = models.CharField(max_length=100)
    u_status = models.IntegerField(default=0)
    addtime = models.DateTimeField(default=datetime.now)
    modifytime = models.DateTimeField(default=datetime.now)
    avatar = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)

    class Meta:
        db_table = 'Constructor'
