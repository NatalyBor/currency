"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from main.views import hello_world
from currency.views import list_rates, contact_form, rates_create, rates_update, rates_delete, rates_details, source_list, source_create, source_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', hello_world),
    path('rate/list', list_rates),
    path('contactus', contact_form),
    path('rate/create', rates_create),
    path('rate/update/<int:pk>/', rates_update),
    path('rate/delete/<int:pk>/', rates_delete),
    path('rate/details/<int:pk>/', rates_details),
    path('source/list', source_list),
    path('source/create', source_create),
    path('source/update/<int:pk>/', source_update),
]
