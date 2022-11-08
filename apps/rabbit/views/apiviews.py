from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from apps.rabbit.models import CalcScenario
from apps.rabbit.serializers import CalcScenarioSerializer, CalcScenarioSlugSerializer
from django.db.models import Q

class CalcScenarioAPIView(ListAPIView):
    queryset = CalcScenario.objects.all()
    serializer_class = CalcScenarioSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        public = self.request.query_params.get('public')
        
        if(public==False or public==None):
            return CalcScenario.objects.filter(user = self.request.user)
        else:
            return CalcScenario.objects.filter(Q(user = self.request.user) | Q(is_public =True))
    

class CalcScenarioSlugAPIView(RetrieveAPIView):
    queryset = CalcScenario.objects.all()
    serializer_class = CalcScenarioSlugSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'slug'

    def get_queryset(self): 
        return CalcScenario.objects.filter(user = self.request.user)
           

        



