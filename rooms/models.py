# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from multiselectfield import MultiSelectField 

# Create your models here.
class user(models.Model):
	user_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	profile_image = models.ImageField(null=True)
	join_date = models.DateTimeField()
	location = models.ForeignKey('location', on_delete=models.CASCADE)
	contact = models.ForeignKey('contact', on_delete=models.CASCADE)
	rooms = models.ForeignKey('rooms', on_delete=models.CASCADE)

	def __str__(self):
		return "first name :" + self.first_name + " " + "last Name :" + self.last_name 

class location(models.Model):
	STATE_CHOICES = (
						("maharashtra", "maharashtra"),
						("hariyana", "hariyana"),
						("chattisgarh", "chattisgarh"), 
						("karnataka", "karnataka"),
					)
	address_line1 = models.CharField(max_length=50, null=False, blank=False)
	address_line2 = models.CharField(max_length=50, null=False, blank=False)
	landmark = models.CharField(max_length=50, null=False, blank=False)
	city = models.CharField(max_length=30, null=False, blank=False)
	state = MultiSelectField(max_length=30, null=False, blank=False, choices=STATE_CHOICES)

	def __str__(self):
		return str(self.landmark) + " " + str(self.city) + " "  + str(self.state) 

class contact(models.Model):
	phone = models.CharField(max_length=10, null=False, blank=False)
	email = models. EmailField(max_length=30, null=False, blank=False, unique=True)

	def __str__(self):
		return str(self.phone) + " " + str(self.email)
		

class rooms(models.Model):
	room_id = models.AutoField(primary_key=True);
	title = models.CharField(max_length=100, null=False, blank=False)
	description = models.TextField(max_length=300, null=False, blank=False)
	location = models.TextField(max_length=200, null=False, blank=False)
	offer_price = models.CharField(max_length=30, null=False, blank=False)
	availability = models.BooleanField()
	pub_date = models.DateTimeField(auto_now=True, auto_now_add=False) 

	def __str__(self):
		return str(self.title) + " " + str(self.location)
		
