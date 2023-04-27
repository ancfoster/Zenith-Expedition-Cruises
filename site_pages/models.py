from django.db import models

# Create your models here.
class Enquiry(models.Model):
    '''
    Model for users to send contact messages
    '''
    name = models.CharField(max_length=30, verbose_name='Name')
    email = models.EmailField(max_length=60, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Phone')
    message = models.TextField(max_length=900, verbose_name='Message')


