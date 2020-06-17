from django.db import models

# Create your models here.

class   List(models.Model):
    items = models.CharField(max_length=100)
    class Meta:
        db_table="List"