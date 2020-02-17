from rest_framework import serializers
from .models import Machine

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ('id','name','number','ip','start_time','end_time')


