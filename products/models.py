from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name
class Products(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.CharField(max_length=500)
    rating = models.FloatField()
    def __str__(self):
        return self.title

