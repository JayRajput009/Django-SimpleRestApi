
from django.urls import path

from restapi import urls
from restapi.views import getuserdetails

urlpatterns = [
   path('get-userdetail/',getuserdetails , name='Get api' ),
#    path()
#    path('post-userdetail/')
]
