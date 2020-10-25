from django.db import models
from django.shortcuts import reverse


class TestModel(models.Model):

    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(max_length=150, unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('name_url', kwargs={'slug': self.slug})
