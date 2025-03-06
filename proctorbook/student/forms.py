from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student

class StudentSignupForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    father_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mother_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    father_mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mother_mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    passport_photo = forms.ImageField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'student'
        if commit:
            user.save()
            student = Student.objects.create(
                user=user,
                roll_number=self.cleaned_data['roll_number'],
                name=self.cleaned_data['full_name'],
                email=self.cleaned_data['email'],
                father_name=self.cleaned_data['father_name'],
                mother_name=self.cleaned_data['mother_name'],
                father_mobile=self.cleaned_data['father_mobile'],
                mother_mobile=self.cleaned_data['mother_mobile'],
                address=self.cleaned_data['address'],
                passport_photo=self.cleaned_data['passport_photo'],
            )
            student.save()
        return user
