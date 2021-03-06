from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField( max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Articles (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField( max_length=100)
    email = models.EmailField(max_length=100)
   
    def __str__(self):
        return self.name
    
class Generic_new(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    pin_code = models.IntegerField()
    contact_number = models.IntegerField()
        
    def __str__(self):
        return self.first_name



        