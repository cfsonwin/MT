from django.db import models
from datetime import datetime


# Create your models here.
class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=100, unique=True)
    u_name = models.CharField(max_length=30, default='user')
    u_password = models.CharField(max_length=100)
    pw_salt = models.IntegerField()
    u_status = models.IntegerField(default=0)
    addtime = models.DateTimeField(default=datetime.now)
    modifytime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id': self.admin_id,
                'u_name': str(self.u_name).split('/')[0],
                'Email': self.Email,
                }
    class Meta:
        db_table = 'Administrator'



class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    Email = models.CharField(max_length=100, unique=True)
    u_name = models.CharField(max_length=30, default='user')
    u_password = models.CharField(max_length=100)
    pw_salt = models.IntegerField()
    u_status = models.IntegerField(default=0)
    addtime = models.DateTimeField(default=datetime.now)
    modifytime = models.DateTimeField(default=datetime.now)
    # avatar = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)

    class Meta:
        db_table = 'Constructor'


class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=50, default="virtual product")
    p_status = models.IntegerField(default=0)
    addtime = models.DateTimeField(default=datetime.now)
    modifytime = models.DateTimeField(default=datetime.now)
    avatar = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'product'

class Manufacturer(models.Model):
    m_id = models.AutoField(primary_key=True)
    contact = models.CharField(max_length=50)
    addr = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)
    m_status = models.IntegerField(default=0)
    addtime = models.DateTimeField(default=datetime.now)
    modifytime = models.DateTimeField(default=datetime.now)
    description = models.TextField()
    m_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'manufacturer'

class CPmapping(models.Model):
    id = models.AutoField(primary_key=True)
    c_id = models.IntegerField()
    c_email = models.CharField(max_length=100)
    p_id = models.IntegerField()

    class Meta:
        db_table = 'cpmapping'


class PMmapping(models.Model):
    id = models.AutoField(primary_key=True)
    p_id = models.IntegerField()
    m_id = models.IntegerField()
    m_pnode = models.IntegerField()
    m_Tlevel = models.IntegerField()

    class Meta:
        db_table = 'pmmapping'