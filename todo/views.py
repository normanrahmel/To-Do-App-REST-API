from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer
from telnetlib import STATUS
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.core import serializers


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = []  # permissions.IsAuthenticated

    def create(self, request):
        todo = Todo.objects.create(title=request.POST.get('title', ''),
                                   description=request.POST.get(
                                       'description', ''),
                                   user=request.user,
                                   )
        serialized_obj = serializers.serialize('json', [todo, ])
        return HttpResponse(serialized_obj, content_type='application/json')
