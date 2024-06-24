from rest_framework import serializers # type: ignore
from restapi.models import UserDetails



class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = UserDetails
        fields = '__all__'
        