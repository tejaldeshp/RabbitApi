from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.rabbit.models import CalcScenario, CalcScenarioParam
from apps.rabbit.serializers import CalcScenarioSerializer
from django.db.models import Q

class CalcScenarioAPIView(APIView):
    @staticmethod
    def get(request):

        #if user unauthorised
        if request.user.is_anonymous:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        #getting query params or is_public
        public = request.query_params.get('public')
        # res_status = status.HTTP_400_BAD_REQUEST
        
        if(public==False or public==None):
            #users' records
            obj = CalcScenario.objects.filter(user = request.user)
        else:
            #user's records or public records
            obj = CalcScenario.objects.filter(Q(user = request.user) | Q(is_public =True))
        
        serializer = CalcScenarioSerializer(obj, many=True)

        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

class CalcScenarioSlugAPIView(APIView):
    pass

