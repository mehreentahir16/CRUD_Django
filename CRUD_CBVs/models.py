from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.IntegerField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('CRUD_CBVs:movie_edit', kwargs={'pk': self.pk})
