from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.get),
    path("diabetes/name=<name>,gluc=<gluc>,bp=<bp>,tri=<tri>,ins=<ins>,bmi=<bmi>",views.dia),
]
