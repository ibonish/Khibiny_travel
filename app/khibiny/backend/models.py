from django.db import models


SEASON_CHOICES = (
    ('winter', 'Зима'),
    ('summer', 'Лето'),
)


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.description


class TravelCard(models.Model):
    name = models.CharField(
        max_length=100
    )
    small_description = models.CharField(
        max_length=500
    )
    season = models.CharField(
        max_length=10,
        choices=SEASON_CHOICES
    )
    description = models.TextField(
        max_length=500
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
