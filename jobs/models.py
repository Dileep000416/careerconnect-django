from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    JOB_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
        ('remote', 'Remote'),
        
)
    EXPERIENCE_LEVEL_CHOICES = (

    ('fresher', 'Fresher'),

    ('junior', 'Junior'),

    ('mid', 'Mid Level'),

    ('senior', 'Senior'),

)
    

    recruiter = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=255
    )

    company_name = models.CharField(
        max_length=255
    )
    company_logo = models.ImageField(
    upload_to='company_logos/',
    blank=True,
    null=True
    )

    location = models.CharField(
        max_length=255
    )

    salary = models.CharField(
        max_length=100
    )

    job_type = models.CharField(
        max_length=50,
        choices=JOB_TYPE_CHOICES
    )
    experience_level = models.CharField(
    max_length=50,
    choices=EXPERIENCE_LEVEL_CHOICES,
    default='fresher'
)

    description = models.TextField()

    requirements = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.title