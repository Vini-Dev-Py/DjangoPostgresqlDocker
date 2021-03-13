from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Produto
from .serializers import ProdutoSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class ProdutoViewSet(viewsets.ModelViewSet):

    serializer_class = ProdutoSerializer

    queryset = Produto.objects.all()