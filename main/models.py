from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    time = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=255)
    ratings = models.DecimalField(max_digits=2, decimal_places=1)
    image_url = models.URLField(blank=True, null=True)

    @property
    def recommend_to_user(self):
        return self.ratings >= 3.7
    

