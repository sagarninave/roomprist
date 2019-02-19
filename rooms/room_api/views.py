from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import (
	CreateAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	DestroyAPIView
	)
from . serializers import UserSerializer
from rooms.models import user

class ListUser(ListAPIView):
    serializer_class = UserSerializer