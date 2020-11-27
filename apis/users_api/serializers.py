from rest_framework import serializers

from ..models import UserApiModel

class ShortUserApiSerialzer(serializers.ModelSerializer):
    class Meta:
        model = UserApiModel
        fields = ['id','first_name','last_name',
                  'full_name','username',
                  'email','phone_number']


class UserApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserApiModel
        fields = ['id','first_name','last_name','full_name',
                  'username','gender','birthday','birth_place',
                  'email','phone_number','address',]
    
    

        

    
    