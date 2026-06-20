from rest_framework import serializers
from . models import Tarea


class TareaSerialaizer(serializers.ModelSerializer):
    class Meta: 
        model = Tarea
        fields = = ['id','titulo','descripcion','compeltado']
        read