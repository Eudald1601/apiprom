from django.db import models

# Create your models here.
class Querys(models.Model):
    created_at = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=50)
    query = models.CharField(max_length=300)

    def __str__(self) -> str:
        return (f"{self.username} {self.query}")