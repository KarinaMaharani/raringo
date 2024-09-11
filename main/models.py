from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    tags = models.CharField(max_length=255)
    ratings = models.DecimalField(max_digits=2, decimal_places=1)

    @property
    def recommend_to_user(self):
        return self.ratings >= 3.7