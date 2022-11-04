from django.urls import path

from apps.rabbit.views.apiviews import *

app_name = 'rabbit_api'

urlpatterns = [
    path('scenarios/', CalcScenarioAPIView.as_view(), name='userslist'),
    path('scenarios/<slug:slug>/', CalcScenarioSlugAPIView.as_view(), name='slug')
]