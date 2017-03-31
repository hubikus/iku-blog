from .models import Sms
from rest_framework import serializers

class SmsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sms
        fields = ('to', 'text')