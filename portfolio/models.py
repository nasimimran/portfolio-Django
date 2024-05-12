from django.db import models


# Create your models here.

class Contacted(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    description = models.CharField(max_length=3000)

    objects = models.Manager()

    class Meta:
        db_table = "contacted"

    def __str__(self):
        return f"{self.name} {self.email}"
