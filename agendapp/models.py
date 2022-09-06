from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, help_text='30 caracteres max.')
    lastname = models.CharField(max_length=30, help_text='30 caracteres max.')
    phone = models.IntegerField(validators=[RegexValidator(r'^\d{6,10}$')], help_text='Min 6 - 10 caracteres max.')
    email = models.EmailField(max_length=30)
