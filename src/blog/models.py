from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    price = models.CharField(max_length=10)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=False)
    image_sec = models.ImageField(upload_to='images', blank=False)
    image2_third = models.ImageField(upload_to='images', blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})