from django.db import models
from django.utils.timezone import get_current_timezone

# Create your models here.                                                                   data is being fetched

class Product(models.Model):
    name = models.CharField(max_length = 100)   # becomes varchar
    price = models.PositiveIntegerField()  # becomes unsigned int
    description = models.TextField() # becomes long or medium text
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True) # stores the curdatetime() in a datetime field
    pic = models.ImageField(upload_to="products/", null = True)

    def __str__(self):                 #to show the object in the Django admin site
        return f'{self.name} - {self.price}'

