from rest_framework import generics , status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView , TokenVerifyView # type: ignore
from rest_framework.generics import UpdateAPIView , GenericAPIView
from django.contrib.auth import get_user_model
from ...models import Profile
from django.core.mail import send_mail
from mail_templated import send_mail # type: ignore
from mail_templated import EmailMessage # type: ignore
from .utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
import jwt # type: ignore
from jwt.exceptions import ExpiredSignatureError , InvalidSignatureError # type: ignore
from django.conf import settings

user   = get_user_model()

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer



    def post(self , request , *args , **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {
                'email' : email
            }
            user_obj = get_object_or_404(User , email = email)
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation_email.tpl' ,  {'token':token} , 'fahimreza20200@gmail.com' , to=['fahimreza2200@gmail.com'])
            EmailThread(email_obj).start()
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    



    def get_tokens_for_user(self ,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomObtainAuthTokenSerializer
    def post(self , request , *args , **kwargs):
        serializer = self.serializer_class(data = request.data , context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user = user)
        return Response({
            'token':token.key,
            'user_id' : user.pk,
            'email': user.email
        })



class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]


    def post(self , request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    


class CustomTokenRefreshView(TokenRefreshView):
    pass

class CustomTokenVerifyView(TokenVerifyView):
    pass



class CustomChangePasswordApi(GenericAPIView):
    serializer_class = ChangePasswordApiSerializer
    model = user
    permission_classes = [IsAuthenticated]


    def get_object(self):
        obj = self.request.user
        return obj
    

    def put(self , request , *args , **kwargs): 
        self.object = self.get_object()
        serializer = self.get_serializer(data= request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password' : ["Wrong Password."]} , status=status.HTTP_400_BAD_REQUEST)
            

            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()

            return Response({'detail':'password changed success .'} , status=status.HTTP_200_OK)
        return Response(serializer.error , status=status.HTTP_400_BAD_REQUEST)
    



class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset , user = self.request.user)
        return obj
    


class TestEmailSend(generics.GenericAPIView):
    def get(self , request , *args , **kwargs):
        self.email = "Fahimreza20200@gmail.com"
        user_obj = get_object_or_404(User , email = self.email)
        token = self.get_tokens_for_user(user_obj)


        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "from@example.com",
        #     ["Fahimreza20200@gmail.com"],
        #     fail_silently=False,
        # )
        # from time import sleep

        # send_mail('email/hello.tpl' ,  {'name':'ali'} , 'fahimreza20200@gmail.com' , ['fahimreza2200@gmail.com'])
        # sleep(2)

        # messages = EmailMessage('email/hello.tpl' ,  {'name':'ali'} , 'fahimreza20200@gmail.com' , to=['fahimreza2200@gmail.com'])
        # messages.send()
    

        email_obj = EmailMessage('email/hello.tpl' ,  {'token':token} , 'fahimreza20200@gmail.com' , to=['fahimreza2200@gmail.com'])
        EmailThread(email_obj).start()

        return Response("Email Send")



    def get_tokens_for_user(self ,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    

class ActivationApiView(APIView):
    def get(self , request , token , *args , **kwargs):
        # Decode -> id user
        try:
            token = jwt.decode(token , settings.SECRET_KEY , algorithms=["HS256"])
            user_id = token.get('user_id')
        except ExpiredSignatureError:
            return Response({'detailS':'Token Has Been Expired . '} , status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({'detailS':'Token Is Not Valid . '} , status=status.HTTP_400_BAD_REQUEST)
        # get object by id
        user_obj = get_object_or_404(User , pk=user_id)
        if user_obj.is_verified:
            # valid response ok
            return Response({'details' : 'your account is verified .'})
        else :
            # user is_verified -> True
            user_obj.is_verified = True
            user_obj.save()
            return Response({'details' : 'your account have been verified and activated successfully .'})
        

class ActivationResentApiView(generics.GenericAPIView):
    serializer_class = ActivationResnetApiSerializer

    def post(self , request , *args, **kwargs):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            user_obj = serializer.validated_data['user']    
            token = self.get_tokens_for_user(user_obj)
            email_obj = EmailMessage('email/activation_email.tpl' ,  {'token':token} , 'fahimreza20200@gmail.com' , to=[user_obj.email])
            EmailThread(email_obj).start()
            return Response({"details" : 'user activation resent successfully .'} , status=status.HTTP_200_OK)
            
    def get_tokens_for_user(self ,user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)
    

