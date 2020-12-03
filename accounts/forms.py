from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class UserLoginForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)

        if not qs.exists():
            raise forms.ValidationError('Пользователь с таким именем не зарегестрирован')

        return username


class UserSignupForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)

        if qs.exists():
            raise forms.ValidationError('Данное имя пользователя уже занято')

        return username
