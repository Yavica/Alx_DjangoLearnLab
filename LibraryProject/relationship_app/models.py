from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
