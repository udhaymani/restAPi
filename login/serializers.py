from rest_framework import serializers
from login import models
class HelloSerializer(serializers.Serializer):
    '''Testing the Serializers'''
    name = serializers.CharField(max_length=10)

#by default modekSerializer allows to create simple object in database
#it uses default create function

class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializes the user profile object'''
    #helps to set the serializer to userprofile model
    class Meta:
        model = models.UserProfile
        fields =('id','email','password','name')
        #to make the password field as write only

        extra_kwargs ={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }

    def create(self,validated_data):
       ''' create & returns new user'''
       user = models.UserProfile.objects.create_user(
           email = validated_data['email'],
           name=validated_data['name'],
           password=validated_data['password']
       )     

       return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)   

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}