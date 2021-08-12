from rest_framework import serializers
from .models  import Motoneiges


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motoneiges
        fields = ('id','year', 'name', 'price')