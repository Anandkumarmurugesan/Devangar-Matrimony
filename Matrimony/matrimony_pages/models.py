from django.db import models
from django.contrib.auth.models import User

# Model variables


# Create your models here.
class Bride(models.Model):
    name = models.CharField(max_length=200,null=True)
    age = models.IntegerField(null=True)
    thegai = models.CharField(max_length=200,null=True)
    State =  models.CharField(max_length=50,null=True)
    District = models.CharField(max_length=50,null=True)
    Address = models.TextField(null=True)
    Phone = models.BigIntegerField(null=True)
    profession = models.CharField(max_length=200,null=True)
    salary = models.BigIntegerField(null=True)
    Under_Graduation_Degree = models.CharField(max_length=200,null=True)
    Under_Graduation_college = models.CharField(max_length=400,null=True)
    Post_Graduation_Degree = models.CharField(max_length=200,null=True)
    Post_Graduation_college = models.CharField(max_length=400,null=True)
    Rasi = models.CharField(max_length=200,null=True)
    Nakshatra = models.CharField(max_length=200,null=True)
    Creator  =  models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Image  = models.ImageField(null=True,blank=True,upload_to="img/%y")
    def __str__(self):
        return self.name
