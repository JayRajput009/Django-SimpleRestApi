from djangorestapi.serializer import UserDetailsSerializer
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from restapi.models import *

# Create your views here.

@api_view(['GET'])
def getuserdetails(request):
    userfeilds = UserDetails.objects.all()
    userserializer = UserDetailsSerializer(userfeilds, many= True)
    serializerdata = userserializer.data
    return Response(
        {
            'status':'True',
            'message':'Get api hit !',
            'data': serializerdata
        }
    )

# @api_view(['POST'])
# def postuserdetails(request):

#     return Response()



