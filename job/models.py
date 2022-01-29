from django.db import models
from django.urls import reverse


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("job-detail", kwargs={"pk": self.pk})
    
