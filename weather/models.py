from django.db import models


class City(models.Model):
    city = models.TextField(max_length=25)

    class Meta:
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.city
