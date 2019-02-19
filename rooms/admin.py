# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rooms.models import user, location, contact, rooms

# Register your models here.
admin.site.register(user)
admin.site.register(location)
admin.site.register(contact)
admin.site.register(rooms)