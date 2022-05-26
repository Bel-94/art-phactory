from django.db import models
# from cloudinary.models import CloudinaryField 

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=100)  

class Category(models.Model):
    cat_name = models.CharField(max_length=100)

class Image(models.Model):
    
    image_name =models.CharField(max_length=200)
    description =models.TextField()
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,default='0')
    location = models.ForeignKey(Location ,on_delete=models.DO_NOTHING,default='0')
    # image=models.ImageField(upload_to='img/',blank = True)
    # image = CloudinaryField('image')
    


