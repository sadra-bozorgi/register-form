from django.shortcuts import render
from .forms import UserRegisterForms
from .models import RegisteredUser
from .sms_utils import send_sms

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForms(request.POST) 
        if form.is_valid():
            cd = form.cleaned_data
            new_user = RegisteredUser.objects.create(
                user_name=cd['user_name'],
                email=cd['email'],
                last_name=cd['last_name'],
                frist_name=cd['frist_name'],
                password=cd['password_1'],
                phone_number=cd['phone_number'],
                City=cd['City'],
            )
            send_sms(cd['phone_number'], cd['user_name'])
            
            return render(request, 'account/success.html')
    else:
        form = UserRegisterForms()
    return render(request, 'account/register.html', {'form': form})