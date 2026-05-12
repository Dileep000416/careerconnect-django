from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class RegisterForm(UserCreationForm):

    ROLE_CHOICES = (
        ('candidate', 'Candidate'),
        ('recruiter', 'Recruiter'),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter email'
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter password'
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm password'
            }
        )
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )

    class Meta:
        model = User

        fields = [
            
            'username',
            'email',
            'role',
            'password1',
            'password2'
        ]

    def save(self, commit=True):

        user = super().save(commit=False)

        if commit:

            user.save()

            UserProfile.objects.create(
                user=user,
                role=self.cleaned_data['role']
            )

        return user
    
class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = [

            'full_name',
            'profile_image',
            'bio',
            'skills',
            'education',
            'experience',
            'resume'
        ]

        widgets = {

            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter full name'
                }
            ),

            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Write about yourself'
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
                    'rows': 4,
                    'placeholder': 'Education details'
                }
            ),

            'experience': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Experience details'
                }
            ),

        }