from django.db import models
from django.urls import reverse

class  Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=100000)
    summary=models.TextField(blank=True,null=True)
    featured=models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
    