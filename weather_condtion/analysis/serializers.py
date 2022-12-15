from .models import Weather, Weather_Yield
from rest_framework import serializers 

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = "__all__"

class WeatherYieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather_Yield
        fields = "__all__"


    