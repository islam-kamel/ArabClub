from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from logging_manager import eventslog
from permissions.permissions import IsOwner
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import CreateUserSerializer, UserSerializer

user_model = get_user_model()
logger = eventslog.logger


class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.validated_data)
            logger.info(
                "{} - Just joined".format(serializer.validated_data.get("username"))
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"{serializer.errors} - {request} - {request.user}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserInfo(APIView):
    permission_classes = [IsOwner]

    def get_object(self, username):
        obj = get_object_or_404(get_user_model(), username=username)
        self.check_object_permissions(self.request, obj)
        return obj

    def put(self, request, username):
        user_object = self.get_object(username)
        serializer = UserSerializer(instance=user_object, data=request.data)
        if serializer.is_valid():
            serializer.update(
                instance=user_object, validated_data=serializer.validated_data
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
