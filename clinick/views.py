from django.shortcuts import render, redirect
from .models import SiteSetting, Slider, CustomerInfo
from .forms import CustomerInfoForm
from django.contrib import messages
from django.conf import settings
import requests

# Create your views here.
def index(request):   
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        # customerinfoForm = customerinfoForm(request.POST)

        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            form = CustomerInfoForm(request.POST, request.FILES)
            if form.is_valid():
                post = CustomerInfo()
                post.name = request.POST.get("name")
                post.address = request.POST.get("address")
                post.subject = request.POST.get("subject")
                post.phone = request.POST.get("phone")
                post.save()
                messages.success(request, 'درخواست شما با موفقیت ثبت شد لطفا منتظر تماس کارشنسان ما باشید', 'success')
                return redirect('landingPage')
            else:
                slider = Slider.objects.filter(status=True)
                info = SiteSetting.objects.last()
                context = {
                    "GOOGLE_RECAPTCHA_SITE_KEY": settings.GOOGLE_RECAPTCHA_SITE_KEY,
                    'sliders': slider,
                    'form': form,
                    'info': info,
                }
                messages.warning(request, 'فرم درخواست مورد تایید نگردید لطفا مجدد تلاش نمایید','warning')
                return redirect('landingPage')
        else:
            return redirect('landingPage')
    else:

        slider = Slider.objects.filter(status=True)
        info = SiteSetting.objects.last()
        form = CustomerInfoForm()
        context = {
            "GOOGLE_RECAPTCHA_SITE_KEY": settings.GOOGLE_RECAPTCHA_SITE_KEY,
            'sliders': slider,
            'form': form,
            'info': info,
        }
        return render(request, 'index.html', context)

def error(request):
    return render(request, '404.html')