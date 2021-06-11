from rest_framework import serializers
from .models import Assignment

class assignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ["id","name","title","description","type","duration","tags"]