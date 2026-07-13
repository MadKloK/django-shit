from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        
        return user

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Invalid Credentials.')
        
        return email
    

class CustomAuthenticationForm(AuthenticationForm):

    def clean(self):
        identifier = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            username = User.objects.get(email=identifier).username
        except User.DoesNotExist:
            username = identifier

        self.user_cache = authenticate(
            request=self.request,
            username=username,
            password=password,
        )

        if self.user_cache is None:
            raise self.get_invalid_login_error()

        self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data