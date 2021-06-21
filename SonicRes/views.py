from django.shortcuts import render
from django.http import HttpResponse
from .models import testupload


# Create your views here.
def index(request):
    return render(request , 'SonicRes/SonicIndex.html')

def upload(request):
    if request.method == "POST":
        test = testupload(filex = request.FILES['myFile'])
        test.save()
        print("hiii" , request.FILES)
        return HttpResponse("maybe")
