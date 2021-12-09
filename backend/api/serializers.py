from django.db.models import fields
from rest_framework import serializers
from metals.models import Metal

class MetalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metal
        fields = '__all__'