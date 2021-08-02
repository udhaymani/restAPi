from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Testing the Serializers'''
    name = serializers.CharField(max_length=10)
