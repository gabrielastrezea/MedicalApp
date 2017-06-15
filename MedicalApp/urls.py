"""MedicalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name="login"),
    url(r'^admin/', admin.site.urls),
    url(r'^medicines/$', views.list_of_medicines, name="list_of_medicines"),
    url(r'^doctors/$', views.list_of_doctors, name="list_of_doctors"),
    url(r'^patients/$', views.list_of_patients, name="list_of_patients"),
    url(r'^add_medicine/$', views.add_medicine, name="add_medicine"),
    url(r'^edit_medicine/(?P<medicine_pk>\d+)$',
        views.add_medicine, name="edit_medicine"),
]