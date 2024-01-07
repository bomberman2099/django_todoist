from django.db import models




class UserProfile(models.Model):
    username = models.CharField(max_length=45)
    Email = models.EmailField()
    password = models.CharField(max_length=70)
    password2 = models.CharField(max_length=70)




