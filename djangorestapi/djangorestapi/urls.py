
from django.contrib import admin
from django.urls import path,include

from restapi import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', urls.restapi, )
]
