from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=20)
    msg = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    role = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='teachers_image/', default="")

    def __str__(self):
        return self.name

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
