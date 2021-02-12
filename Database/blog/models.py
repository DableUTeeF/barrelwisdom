from django.db import models
from django.conf import settings

class Section(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, default='')
    slugtitle = models.CharField(max_length=200, blank=True, default='')
    body = models.TextField()
    image = models.CharField(max_length=255, default='', blank=True)
    description = models.CharField(max_length=200, default='')
    authorlock = models.BooleanField(default=False)
    author = models.ManyToManyField(settings.AUTH_USER_MODEL)
    tags = models.ManyToManyField(Tags, blank=True,)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default="1")

    class Meta:
        ordering = ['created']
        unique_together = ['slugtitle', 'section']