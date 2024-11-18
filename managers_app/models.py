from django.db import models
from django.db.models import Avg

class CustomManager(models.Manager):
    def average_reviews(self):
        return self.annotate(avg_rating=Avg('reviews__rating'))

class BookModel(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    objects = models.Manager()
    custom_manager = CustomManager()


class ReviewModel(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField()
    rating = models.PositiveIntegerField()
