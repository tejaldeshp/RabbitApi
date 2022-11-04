from rest_framework import serializers
from apps.rabbit.models import CalcScenario, CalcScenarioParam

class CalcScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalcScenario
        fields = ('id', 'slug', 'name', 'user')


