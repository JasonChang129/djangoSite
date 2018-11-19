from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    color = models.CharField(max_length=64)
    page_num = models.IntegerField(null=True)
    publisher = models.ForeignKey('Publish',on_delete=models.CASCADE) #一对多关系
#
#     #接受对象
#     author = models.ManyToManyField('Author')
    def __str__(self):
        return self.title

class Publish(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=32)
#
#     def __str__(self):
#         return self.name

# class AuthorDetail(models.Model):
#     sex = models.BooleanField(max_length=1,choices=((0,'男'),(1,'女')))
#     email = models.EmailField()
#     address = models.CharField(max_length=50)
#     birthday = models.DateField()
#     author = models.OneToOneField(Author,on_delete=models.CASCADE)