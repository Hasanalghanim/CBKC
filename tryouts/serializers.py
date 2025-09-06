from rest_framework import serializers
from .models import TryoutEvent,TryoutRegistrant

class TryoutEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryoutEvent
        fields = '__all__' 




class TryoutRegistrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = TryoutRegistrant
        fields = '__all__' 