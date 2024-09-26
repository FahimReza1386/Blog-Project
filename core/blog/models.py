from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User=get_user_model()

class Post(models.Model):

    """
        this is a class to define posts for blog app
    """

    author = models.ForeignKey('accounts.Profile' , on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content= models.TextField()
    status=models.BooleanField()
    category = models.ForeignKey('Category' , on_delete=models.SET_NULL , null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()



    def __str__(self):
        return f'{self.title}'
    

class Category(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return f'{self.name}'