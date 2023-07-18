from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import Booth
from .serializers import BoothSerializer


class BoothAPIView(APIView):
    def get(self,format=None):
        queryset=Booth.objects.all()
        serializer=BoothSerializer(queryset,many=True)
        
        return Response(serializer.data,status=HTTP_200_OK)
   
    
    