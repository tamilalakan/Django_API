from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Account
from . serializers import AccountSerializer

from rest_framework import viewsets
from . import models
from . import serializers


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import Account
from account.serializers import AccountSerializer




def register(request):
	return render(request,"account/view.html")


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Account.objects.all()
        serializer = AccountSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sni = Account.objects.all()
            ser = AccountSerializer(sni,many=True)
            return render(request,'account/final_view.html',{"data":serializer.data,"data1":ser.data})
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	



class AccountViewset(viewsets.ModelViewSet):
	queryset = models.Account.objects.all()
	serializer_class = serializers.AccountSerializer

