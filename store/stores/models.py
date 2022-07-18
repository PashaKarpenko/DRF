from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=800)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='stores', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(choices=(('active', 'Active'), ('deactivated', 'Deactivated'), ('in_review', 'In review')),
                              max_length=20, default='in_review')

    def __str__(self):
        return f'{self.name} {self.description}, {self.rating}'

    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
