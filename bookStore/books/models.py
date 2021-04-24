from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Category (models.Model):
    class Meta:
        verbose_name_plural="categories"
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Isbn (models.Model):
    isbn_num=models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    author_title=models.CharField(max_length=256)
    book_title=models.CharField(max_length=256)
    def __str__(self):
        return str(self.isbn_num )
class Tag(models.Model):
    name=models.CharField( max_length=25)   
    def _str_(self):
         return str(self.name)


class Book(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField(max_length=2048)
    auther= models.ForeignKey(User, on_delete=models.CASCADE, related_name="books" , null=True,blank=True)
    categories=models.ManyToManyField(Category)
    isbn=models.OneToOneField(Isbn, on_delete=models.CASCADE, null=True,blank=True)
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE,null=True,blank=True)



    def __str__(self):
        return self.title
