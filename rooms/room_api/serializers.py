from rest_framework.serializers import ModelSerializer
from rooms.models import user

class UserSerializer(ModelSerializer):
	class Meta:
		model = user
		fields = '__all__'