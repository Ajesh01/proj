from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.get),
    path("diabetes/name=<name>,gluc=<gluc>,bp=<bp>,tri=<tri>,ins=<ins>,bmi=<bmi>",views.dia),
    path("heart/age=<age>,sex=<sex>,cp=<cp>,trestbps=<trestbps>,chol=<chol>,fbs=<fbs>,restecg=<restecg>,thalach=<thalach>,exang=<exang>,oldpeak=<oldpeak>,slope=<slope>,ca=<ca>,thal=<thal>",views.hea),
]
