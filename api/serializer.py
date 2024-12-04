from rest_framework import serializers
from .models import programmer

class programmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer 
        #fields= ('fullname', 'nickname', 'age')
        fields= '__all__'