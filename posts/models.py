# Import django.db.models
from django.db import models

# Import django.urls.reverse
from django.urls import reverse

from ckeditor.fields import RichTextField

# Get User 
from django.contrib.auth import get_user_model

# Model
class Post(models.Model):
    """ Model For Post """

    # Fields
    
    category = models.TextField()
    title = models.TextField()
    summary = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True)
    body = RichTextField()

    # Add Posted Time Automaticly
    date = models.DateField(auto_now=True)

    # Author
    # author = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])
