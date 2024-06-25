from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import StudentClassSelectionSerializer, UserRegestrationSerializer,UserLoginSerializer,UserProfileSerializer,UserChangePasswordSerializer,SendPasswordResetEmailSerializer , UserPasswordResetSerializer 
from django.contrib.auth import authenticate ,login
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from accounts.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from accounts.utils import Util
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

# generate token manully 
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
# end of functiion

# register user function 
class UserRegestrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request , formate =None):
        serializer= UserRegestrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            
            # Generate OTP
         # Generate OTP with creation time
            otp, otp_created_at = Util.generate_otp()
            
            # Store OTP and creation time in session
            request.session['temp_user_data'] = serializer.validated_data
            request.session['otp'] = otp
            request.session['otp_created_at'] = otp_created_at  # Store OTP creation time

            
            # Send OTP to the user's email
            email_data = {
                'subject': 'Your OTP for Registration',
                'body': f'Your OTP for registration is {otp}. Please enter this code to complete your registration.',
                'to_email': email
            }
            try:
                Util.send_mail(email_data)
                return Response({'msg': 'OTP sent to your email. Please verify to complete registration.'}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)        
         

        
        return Response({'msg': 'Registration unsuccessful'}, status=status.HTTP_400_BAD_REQUEST)
# end of register user function

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    
    def post(self, request , formate = None):
        
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email = email , password = password )
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token' : token ,'msg' : 'Login successfull'},status=status.HTTP_200_OK)
            else:
                return Response({'errors' : {'non_field_errors' : ['email or Password is not valid']}} ,status=status.HTTP_404_NOT_FOUND)
            
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self, request , formate = None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data , status= status.HTTP_200_OK)
    

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request , formate = None):
        serializer = UserChangePasswordSerializer(data= request.data , context = {'user' : request.user})
        if serializer.is_valid(raise_exception=True):
            return  Response({'msg' : 'password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)


class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self , request , formate = None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return  Response({'msg' : 'password reset link is sent to your email please check your email'}, status=status.HTTP_200_OK)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class  UserPasswordResetView(APIView):
    renderer_classes = [ UserRenderer]
    def post(self , request , uid, token ,formate = None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)

class StudentClassSelectionView (APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request , formate = None):
        serializer = StudentClassSelectionSerializer(data=request.data, instance=request.user)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            selected_class = user.student_class
            return Response({'msg': 'Class selection updated successfully', 'selected_class': selected_class}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserUnregisterView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, format=None):
        user = request.user
        user.delete()
        return Response({'msg': 'User unregistered successfully'}, status=status.HTTP_200_OK)
    

class VerifyOTPView(APIView):
    def post(self, request, format=None):
        print("heloo")
        otp = request.data.get('otp')
        print(otp)
        stored_otp = request.session.get('otp')
        print(otp == stored_otp)
        print(stored_otp)
        otp_created_at = request.session.get('otp_created_at')
        
        if otp == stored_otp and not Util.is_otp_expired(otp_created_at):
            temp_user_data = request.session.get('temp_user_data')
            if temp_user_data:
                serializer = UserRegestrationSerializer(data=temp_user_data)
                if serializer.is_valid():
                    user = serializer.save()
                    token = get_tokens_for_user(user)
                    # Clean up session data
                    del request.session['temp_user_data']
                    del request.session['otp']
                    del request.session['otp_created_at']
                    return Response({'token': token, 'msg': 'Registration successful'}, status=status.HTTP_201_CREATED)
        
        return Response({'msg': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)