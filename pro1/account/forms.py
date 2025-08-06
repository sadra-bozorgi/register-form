from django import forms
from .models import RegisteredUser
from django.core.exceptions import ValidationError
import re

class UserRegisterForms(forms.Form):
    user_name = forms.CharField(max_length=50, label='Username')
    email = forms.EmailField(label='Email')
    frist_name = forms.CharField(max_length=50, label='Fristname')
    last_name = forms.CharField(max_length=50, label='Lastname')
    password_1 = forms.CharField(max_length=50, label='Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(max_length=50, label='Repeat password', widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=11, label='Phonenumber') 
    City = forms.CharField(max_length=50, label='Country')

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if RegisteredUser.objects.filter(email=email).exists():
            raise ValidationError("این ایمیل قبلاً ثبت شده است")
        return email
    

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if RegisteredUser.objects.filter(user_name=user_name).exists():
            raise ValidationError("این نام کاربری قبلاً ثبت شده است")
        return user_name
    

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if RegisteredUser.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("این شماره موبایل قبلاً ثبت شده است")
       
        if not re.fullmatch(r"09\d{9}", phone_number):
            raise ValidationError("فرمت شماره موبایل نامعتبر است (مثال: 09123456789)")
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password_1")
        password2 = cleaned_data.get("password_2")

        if password1 != password2:
            raise ValidationError("رمزها با هم مطابقت ندارند")

        if password1 and len(password1) < 8:
            raise ValidationError("رمز عبور باید حداقل ۸ کاراکتر باشد")
         
        if not re.search(r'[A-Z]', password1):
            raise ValidationError("رمز باید حداقل یک حرف بزرگ داشته باشد")

    
        if not re.search(r'[a-z]', password1):
            raise ValidationError("رمز باید حداقل یک حرف کوچک داشته باشد")

    
        if not re.search(r'[0-9]', password1):
            raise ValidationError("رمز باید حداقل یک عدد داشته باشد")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
            raise ValidationError("رمز باید حداقل یک علامت خاص داشته باشد")
