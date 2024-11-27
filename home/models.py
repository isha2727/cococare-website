
from django.db import models

# makemigration-create changes and store in a file
# migrate-apply the changes to the database
# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
