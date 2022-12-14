from django.db import models
class Memberships(models.Model):
    name = models.CharField(max_length=150)
    validity = models.PositiveIntegerField()
    price = models.PositiveIntegerField(null=True)
    desc = models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to="images/",null=True,blank=True)
    status=models.BooleanField(default=True,null=True)


    def __str__(self):
        return self.name