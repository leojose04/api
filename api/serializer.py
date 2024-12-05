from rest_framework import serializers
from .models import programmer
from .models import Stu

class programmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer 
        #fields= ('fullname', 'nickname', 'age')
        fields= '__all__'

class StuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stu
        #fields= ('fullname', 'nickname', 'age')
        fields= '__all__'