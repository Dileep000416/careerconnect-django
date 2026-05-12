from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
    max_length=200,
    blank=True
)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
         default='candidate'
    )

    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True,
        null=True
    )

    skills = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    education = models.TextField(
        blank=True,
        null=True
    )

    experience = models.TextField(
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    company_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    company_website = models.URLField(
        blank=True,
        null=True
    )

    company_description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):

        return self.user.username