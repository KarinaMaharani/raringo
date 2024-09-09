from django.db import models

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=255)
    ratings = models.DecimalField(max_length=2)

    @property
    def recommend_to_user(self):
        return self.ratings >= 3.7