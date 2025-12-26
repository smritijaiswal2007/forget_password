from django.shortcuts import render
from .models import student


# Create your views here.
def landing(req):
    return render(req,'landing.html')

def forgetpass(req):
    return render(req,'forgetpass.html')

def resetpass(req):
    
    userdata = student.objects.get(Email=e)
    print(userdata.password)
    userdata.password=n_pass
    userdara.save()
    return render(req,'landing.html',{'msg2':'password reset successfully'})

def send_otp(req):
    if req.method=='POST':
        e = req.POST.get('email')
        otp = random.randint(11111,99999)
        req.session['email'],req.session['otp']=e,otp
        send_mail('subject'
                f'generated otp for django app is {{otp}}',
                '(smritijais999@gmail.com)',
                [e]
                
                )