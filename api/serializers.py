from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'code', 'host', 'title', 'type', 'visible', 'created_at')
        

class CreateResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('title', 'content', 'type', 'visible')