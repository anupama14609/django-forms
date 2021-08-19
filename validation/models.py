from django.db import models

# Create your models here.

class DefaultModel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email= models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self):
        return str(self.firstname)

class CrispyModel(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    likes = models.CharField(max_length=250)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    living = models.CharField(max_length=150, null=True, blank=True)
    def __str__(self):
        return str(self.nickname)

class TweakModel(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3

    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-Book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
    def __str__(self):
        return str(self.title)