from django.conf.urls import url, include
from django.contrib import admin
from . views import ListUser

urlpattern = [
			url(r'^listuser/', ListUser.as_view(), name="listuser"),
]