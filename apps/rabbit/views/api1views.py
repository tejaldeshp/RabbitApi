from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rabbit.models import CalcScenario, CalcScenarioParam
from apps.rabbit.serializers import CalcScenarioSerializer, CalcScenarioSlugSerializer
from django.db.models import Q

class CalcScenarioAPIView(APIView):
    @staticmethod
    def get(request):

        #if user unauthorised
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        #getting query params or is_public
        public = request.query_params.get('public')
        
        if(public==False or public==None):
            #users' records
            obj = CalcScenario.objects.filter(user = request.user)
        else:
            #user's records or public records
            obj = CalcScenario.objects.filter(Q(user = request.user) | Q(is_public =True))
        
        #serialize data
        serializer = CalcScenarioSerializer(obj, many=True)

        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)



class CalcScenarioSlugAPIView(APIView):
    @staticmethod
    def get(request, slug):

        #if user unauthorised
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            #get object with input slug
            obj = CalcScenario.objects.get(Q(user = request.user) & Q(slug=slug))
            #serialize data
            serializer = CalcScenarioSlugSerializer(obj)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

        



