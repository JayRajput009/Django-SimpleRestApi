
from django.urls import path

from restapi import urls
from restapi.views import getuserdetails, postuserdetails

urlpatterns = [
   path('get-userdetail/',getuserdetails , name='Get api' ),
   path('post-userdetail/',postuserdetails, name='Post api')
]
