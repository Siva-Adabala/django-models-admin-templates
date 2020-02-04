from django.db import models

class Author(models.Model):
    name = models.CharField("Author Name",max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Publisher(models.Model):
    name = models.CharField("Publisher Name",max_length=300)
    
    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField("Book Name",max_length=300)
    pages = models.IntegerField("Tot. No. of Pages")
    price = models.DecimalField( "Cost", max_digits=10, decimal_places=2)
    rating = models.FloatField("Rating of Book")
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField("Publication Date")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    

class Store(models.Model):
    name = models.CharField("Store Name", max_length=300)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    