from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse

from app.models.base import BaseModel


class Resource(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resources')

    public_key = models.CharField(max_length=2048)
    public_url = models.URLField(max_length=1024)
    name = models.CharField(max_length=1024)
    owner = models.CharField(max_length=1024)
    yd_created_at = models.DateTimeField()

    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
        unique_together = ['user', 'public_url']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:resource_detail', args=[self.public_url])
