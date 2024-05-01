from django.db import models

# Create your models here.
class Links(models.Model):
    address=models.CharField(max_length=100,null=True,blank=True)
    sname=models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.sname
    