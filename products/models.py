from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name =  models.CharField(max_length=255)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Catagories'
    
    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    name =  models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField(blank = True, null=True)
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    created_by =  models.ForeignKey(User, related_name = 'Products', on_delete=models.CASCADE)
    created_at =  models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Products'
    
    def __str__(self) -> str:
        return self.name

