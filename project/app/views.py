from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def forgetpass(req):
    return render(req,'forgetpass.html')

def resetpass(req):
    return render(req,'resetpass.html')

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