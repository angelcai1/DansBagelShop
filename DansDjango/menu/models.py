from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Option(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='option')
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=5)
    quantity = models.IntegerField(default=100)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    items = models.CharField(max_length=200)
    total = models.IntegerField(default=0)
