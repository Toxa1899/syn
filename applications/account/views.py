from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.serializers import RegisterSerializers


# Create your views here.


class RegisterAPIView(APIView):

    def post(self, request):
        serializers = RegisterSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(
            "Вы успешно зарегистрировались вам отправлено письмо на почту",
            status=201,
        )
