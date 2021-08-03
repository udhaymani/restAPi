from rest_framework.views import APIView
from rest_framework.response import Response
from login import models
from rest_framework import status,viewsets
from login import serializers
# it helps to authenticate the correct Method
from rest_framework.authentication import TokenAuthentication
from login import permissions
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self,request):
        '''Post request to hello API'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =f'Hello,{name}'    

            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST) 

    def put(self,request,pk=None):
        '''Handing updating the object'''

        return Response({'method':'PUT'})

    def patch(self,request,pk=None):

        '''Handle partial update of an object'''
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        '''Handle the Delete request in an object'''
        return Response({'method':'DELETE'})        


class HelloViewSet(viewsets.ViewSet):
    '''Test API View Set'''
    serializer_class = serializers.HelloSerializer
    def list(self,request):

        a_viewset=[
             'Uses HTTP methods as functions (create,read, update, ddd, sss)',
            'Is similar to a traditional Django View',
            'Gives you the most functionality with less code',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','a_viewSet':a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message =f'Hello ,{name}'    

            return Response({'message':message})
        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST) 

    def retreive(self,request,pk=None):
        '''Handing updating the object'''

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):

        '''Handle partial update of an object'''
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        '''Handle the Delete request in an object'''
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        '''Handle the Delete request in an object'''
        return Response({'http_method':'DELETE'})

#to manage the models inside the views
class USerProfileViewSet(viewsets.ModelViewSet):
    '''handle creating & updating the profiles'''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    #it helps to pass the permission to the authenticated user
    permission_classes= (permissions.UpdateOwnProfile,)
