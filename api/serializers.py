from rest_framework import serializers
from api.models import ApiModel
class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiModel
        fields = '__all__'