from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=128, unique=True, null=False)
    starting_date = models.DateField(null=False)
    description = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title
