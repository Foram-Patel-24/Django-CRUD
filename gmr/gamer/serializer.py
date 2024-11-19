from .models import Gamerinfo
from rest_framework import serializers

class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamerinfo
        fields = ['id' , 'username' , 'state' , 'region']