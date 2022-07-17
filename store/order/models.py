from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=800)
    rating = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.description}, {self.rating}'

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
