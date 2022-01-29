from django.db import models
from job.models import Job


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=64, blank=False)
    position_apply = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    resume_file = models.FileField(blank=True, null=True, upload_to='resume')

    def __str__(self):
        return self.first_name
