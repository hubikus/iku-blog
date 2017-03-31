from rest_framework import viewsets
from .models import Sms
from .serializers import SmsSerializer

class SmsViewSet(viewsets.ModelViewSet):
    queryset = Sms.objects.all()
    serializer_class = SmsSerializer