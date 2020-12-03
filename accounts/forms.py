from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)

        if not qs.exists():
            raise forms.ValidationError('Пользователь с таким именем не зарегестрирован')

        return username

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            raise forms.ValidationError('Неверный пароль')

        return password


class UserSignupForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)

        if qs.exists():
            raise forms.ValidationError('Данное имя пользователя уже занято')

        return username
