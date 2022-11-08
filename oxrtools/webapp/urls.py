from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get_files', views.get_files, name="get-files"),
    path('add_aadhar_front', views.add_aadhar_front, name="add_aadhar_front"),
    path('add_aadhar_back', views.add_aadhar_back, name= "add_aadhar_back"),
 ]

#path converters
#path('<int: numbers>/<str:string>', views.function, name='')
