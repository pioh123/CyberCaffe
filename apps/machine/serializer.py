from rest_framework import serializers
from .models import Machine,Game
from rest_framework import generics

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id','name','number','ip','start_time','end_time')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','name','image','url')
