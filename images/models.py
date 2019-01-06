from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=140)
    slug = models.CharField(max_length=140)
    created_at = models.DateTimeField()
    url = models.CharField(max_length=140)
    describtion = models.TextField()

    def __str__(self):
        return 'Image: <name:{}>, <slug:{}>, <created_at:{}>, <url:{}>, <description:{}>'.format(self.name, self.slug, self.created_at, self.url, self.describtion)