from django.urls import path
from SonicRes import views

app_name= 'SonicRes'

urlpatterns = [
    path('index' , views.index , name='index'),
]
