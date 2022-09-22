from django.db import models
from django.urls import reverse

class Wine(models.Model):
    # slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    def get_absolute_url(self):
        return reverse('wines:post_detail', args=[self.pk])
        
    