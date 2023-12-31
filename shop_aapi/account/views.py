from rest_framework.views import APIView

from .serializers import RegisterSerializer
from rest_framework.response import Response
from .models import User


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registerd', 201)
        

class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response(
                'user does not exist', 400
            )
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response(
            'Activated', 200
        )