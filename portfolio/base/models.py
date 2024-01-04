from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank= False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    message = models.TextField()

    def __str__(self):
        return self.name