from django.shortcuts import render
from .models import Gamerinfo
from .serializer import GamerSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter


# Create your views here.

class GamerViewset(ModelViewSet):
    queryset = Gamerinfo.objects.all()
    serializer_class = GamerSerializer
    authentication_class = [BasicAuthentication]
    permission_class = [IsAuthenticatedOrReadOnly]    
    filter_backends = [SearchFilter]
    search_fields = ['^id' , '^username']



'''    def create(self , request , *args , **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created.'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

    def list(self, request, *args, **kwargs , pk = None):
        id = pk
        gmr = Gamerinfo.objects.get(id=pk)
    

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)  '''