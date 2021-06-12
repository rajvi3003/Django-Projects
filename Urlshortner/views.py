from django.shortcuts import render , redirect
from Urlshortner.models import Url
from django.http import HttpResponse
import uuid
# Create your views here.

def index(request):
    SResult = False
    return render(request , 'Urlshortner/Urlindex.html')

def create(request):
    SResult = True
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link , uid=uid)
        new_url.save()
        print(new_url)
        return HttpResponse(uid)

def go(request , sht):
    big_url = Url.objects.get(uid=sht)
    return redirect(big_url.link)
