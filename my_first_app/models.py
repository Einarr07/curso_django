from django.db import models


# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=20, null=True)

    def __str__(self):
        return f'Title: {self.title} year: {self.year} color: {self.color}'


class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField(max_length=200)

    def __str__(self):
        return f'Name: {self.name} addres: {self.address}'


class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return f'Name: {self.name} birth_date: {self.birth_date}'


class Book(models.Model):
    title = models.TextField(max_length=2100)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # One to many
    authors = models.ManyToManyField(Author, related_name='books')  # Many to many

    def __str__(self):
        return f'Title: {self.title} publication_date: {self.publication_date}'
