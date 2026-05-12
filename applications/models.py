from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from jobs.models import Job


class Application(models.Model):
    STATUS_CHOICES = [

    ('applied', 'Applied'),

    ('reviewed', 'Reviewed'),

    ('shortlisted', 'Shortlisted'),

    ('accepted', 'Accepted'),

    ('rejected', 'Rejected'),

]


    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
    max_length=20,
    choices=STATUS_CHOICES,
    default='applied'
)

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.applicant.username} - {self.job.title}"



class SavedJob(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        'jobs.Job',
        on_delete=models.CASCADE
    )

    saved_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            'user',
            'job'
        )

    def __str__(self):

        return f"{self.user.username} saved {self.job.title}"
    

class Notification(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.message