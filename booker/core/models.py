from django.db import models

# Create your models here.
class Type(models.Model):
    Tname = models.CharField(max_length=50)


    def __str__(self):
        return self.Tname

class Transportation(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='transport_images/')
    start = models.CharField(max_length=50,null=True)
    end = models.CharField(max_length=50,null=True)
    vehicletype = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.name
    

