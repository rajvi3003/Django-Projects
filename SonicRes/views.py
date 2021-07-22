from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import testupload

# library for post request
import requests




# Create your views here.
def index(request):
    return render(request , 'SonicRes/SonicIndex.html')


def upload(request):
    if request.method == "POST":
        test = testupload(filex = request.FILES['myFile'] ,title = str(request.FILES['myFile']) , shortUrl = '')
        test.save()
        print(test.filex)
        redirectLink = 'https://parasdjango.pythonanywhere.com/media/'+str(test.filex)
        # redirectLink = 'http://127.0.0.1:8000/media/'+str(test.filex)

        test.shortUrl =  'https://parasdjango.pythonanywhere.com/go/'+shortner(redirectLink)
        # test.shortUrl =  'http://127.0.0.1:8000/go/'+shortner(redirectLink)
        test.save()
        print("Uploaded the file" , request.FILES['myFile'])
        # return HttpResponse(str(test.shortUrl))
        return redirect('/SonicRes/dashboard')


#only used to shortn the file url
def shortner(redirectLink):
    Redirectdata = {'link': redirectLink}
    shortUrl = requests.post(url = 'https://parasdjango.pythonanywhere.com/Urlshortner/create', data = Redirectdata)
    # shortUrl = requests.post(url = 'http://127.0.0.1:8000/Urlshortner/create', data = Redirectdata)
    shortUrl = shortUrl.text
    return shortUrl

def dashboard(request):
    userData = testupload.objects.order_by('title')
    print(userData)
    context = {'records': userData}
    return render(request , "SonicRes/dashboard.html" , context=context)
