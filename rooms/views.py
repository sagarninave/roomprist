from django.http import HttpResponse
from rooms.models import user, location, rooms, contact
from django.template import loader

def index(request):
	data = user.objects.all()
	template = loader.get_template('index.html')
	context = {'data' : data}
	return HttpResponse(template.render(context, request))