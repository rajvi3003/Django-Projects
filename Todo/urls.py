from django.urls import path

from Todo import views

app_name = 'Todo'
urlpatterns = [
    path('index', views.index , name='index'),
    path('create' , views.create , name='create'),
    path('complete/<str:id>' , views.complete , name='complete'),
    path('delete/<str:id>' , views.delete , name='delete'),
]
