from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class SignInForm(AuthenticationForm):

    username = forms.EmailField(label=_('نام کاربری '), required=True, help_text=_('در نظر داشته باشید که نام کاربری همان ایمیل شما میباشد.'))
    password = forms.CharField(label=_('رمز عبور'), widget=forms.PasswordInput, required=True)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')

        try:
            user = User.objects.get(email=username)
            if not check_password(password, user.password):
                 raise ValidationError(_('پسوورد غلطه!!!'))
        except User.DoesNotExist:
            pass
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username)>20:
            raise ValidationError(_('طول ایمیل بیش از حد متعارف میباشد!'))
        try:
            User.objects.get(email=username)
        except User.DoesNotExist:
            raise ValidationError(_('ایمیل کاربری یافت نشد!'))
        return username


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(label=_('تایید پسوورد'), required=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'melli_code', 'password2', 'password')
        labels = {'email': _('ایمیل کاربری '), 'first_name': _('نام'), 'last_name': _('نام خانوادگی'),
                  'password': _('رمز عبور'), 'melli_code': _('کد ملی')}
        widgets = {'email': forms.EmailInput, 'first_name': forms.TextInput,
                   'last_name': forms.TextInput, 'password': forms.PasswordInput,
                   'melli_code': forms.TextInput}

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise ValidationError(_('رمز عبور و تایید رمز عبور مغایر هستند!'))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            us_email = User.objects.get(email=email)
            if us_email:
                raise ValidationError(_('ایمیل موجود میباشد! ایمیل دیگری وارد نمایید'))
        except User.DoesNotExist:
            pass
        return email

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        first_name = self.cleaned_data.get('first_name')
        try:
            user_lastname = User.objects.get(last_name=last_name)
            if user_lastname and user_lastname.first_name == first_name:
                full_name = first_name+' '+last_name
                raise ValidationError(_(f'کاربری با نام  {full_name}  موجود است'))

        except User.DoesNotExist:
            pass
        return last_name

    def clean_melli_code(self):
        melli_code = self.cleaned_data.get('melli_code')
        try:
            us_melli_code = User.objects.get(melli_code=melli_code)
            if us_melli_code:
                raise ValidationError(_(f'کد ملی {melli_code} موجود میباشد '))
        except User.DoesNotExist:
            pass
        return melli_code

