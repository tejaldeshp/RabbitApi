from django.contrib import admin
from apps.rabbit.models import CalcScenario, CalcScenarioParam

class CalcScenarioAdmin(admin.ModelAdmin):
    list_display = ('id','slug','user','is_public','price_per_run')

class CalcScenarioParamAdmin(admin.ModelAdmin):
    list_display = ('id','scenario','param','value')

admin.site.register(CalcScenario, CalcScenarioAdmin)
admin.site.register(CalcScenarioParam, CalcScenarioParamAdmin)

