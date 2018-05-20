from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Movies(models.Model):

    '''by specifying user as Foreign Key, we're using the builtin User model of django.
    You can use the same method for Class Based View too.'''

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('CRUD_FBVs:movies_edit', kwargs={'pk': self.pk})
