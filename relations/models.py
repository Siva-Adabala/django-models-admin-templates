from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE, default = "siva")
    headline = models.CharField(max_length=125)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
    


    
    