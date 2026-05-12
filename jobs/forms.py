from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:

        model = Job

        fields = [
            'title',
            'company_name',
            'company_logo',
            'location',
            'salary',
            'job_type',
            'experience_level',
            'description',
            'requirements',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Job Title'
                }
            ),

            'company_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Company Name'
                }
            ),
            
            'company_logo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Job Location'
                }
            ),

            'salary': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Salary'
                }
            ),

            'job_type': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'experience_level': forms.Select(
    attrs={
        'class': 'form-select'
    }
),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Job Description'
                }
            ),

            'requirements': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Job Requirements'
                }
            ),
        }