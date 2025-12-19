from django.db import models
from django.utils.text import slugify
import uuid

class Result(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='results/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    unique_slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.unique_slug:
            self.unique_slug = slugify(self.title) + "-" + str(uuid.uuid4())[:6]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
