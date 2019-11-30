from django.conf import settings
from django.db import models
from src.common.abstract_model import AbstractModel


class Product(AbstractModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True)

    class Meta:
        default_related_name = 'products'
        db_table = 'products'

    def __str__(self):
        return self.name
