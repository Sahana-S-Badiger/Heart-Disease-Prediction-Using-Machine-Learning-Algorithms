from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class PredictForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.IntegerField(label='Sex (0 for Female, 1 for Male)')
    chest_pain_type = forms.IntegerField(label='Chest Pain Type (0-3)')
    resting_bp = forms.IntegerField(label='Resting BP')
    cholesterol = forms.IntegerField(label='Cholesterol')
    fasting_bs = forms.IntegerField(label='Fasting BS (0 or 1)')
    resting_ecg = forms.IntegerField(label='Resting ECG (0-2)')
    max_hr = forms.IntegerField(label='Max HR')
    exercise_angina = forms.IntegerField(label='Exercise Angina (0 for No, 1 for Yes)')
    oldpeak = forms.FloatField(label='Oldpeak', widget=forms.NumberInput(attrs={'step': 0.1}))
    slope = forms.IntegerField(label='Slope (0-2)')

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match')
        return password2

class SignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
