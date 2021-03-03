from django.db import models

# Create your models here.
class em(models.Model):
    id=models.IntegerField
    username=models.CharField (max_length=255)
    Email_ID= models.EmailField(primary_key=True)
    password=models.CharField(max_length=255)
    def __str__(self):
        return self.username
    