from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls import reverse
from tinymce import HTMLField

from blog.utils import unique_slug_generator
from django.db.models.signals import pre_save

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField()
    document = models.FileField()

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={
    #         'id': self.id
    #     })


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Post)
