from rest_framework import serializers
from apps.rabbit.models import CalcScenario, CalcScenarioParam

class CalcScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalcScenario
        fields = ('id', 'slug', 'name', 'user')


class CalcScenarioSlugSerializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField()

    class Meta:
        model = CalcScenario
        fields = ('id','slug', 'name', 'user', 'result')
    
    @staticmethod
    def get_result(obj):
        result = obj.func_trial()
        # result = obj.enumerate_scenarios()
        return result