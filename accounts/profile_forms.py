from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = [
            'full_name',
            'role',
            'profile_image',
            'bio',
            'skills',
            'education',
            'experience',
            'resume',
            'company_name',
            'company_website',
            'company_description',
        ]

        widgets = {

            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            'skills': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Python, Django, React'
                }
            ),

            'education': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            'experience': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),

            'company_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'company_website': forms.URLInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'company_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4
                }
            ),
        }

    profile_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    resume = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )