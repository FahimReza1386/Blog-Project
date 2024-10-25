from rest_framework import generics , status
from .serializers import *
from rest_framework.response import Response

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer



    def post(self , request , *args , **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()

            data = {
                'email' : serializer.validated_data['email']
            }
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)