from django.urls import path
from . import views

app_name='SonicRes'

urlpatterns = [
    path('index' , views.index , name='name'),
]
