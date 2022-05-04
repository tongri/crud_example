from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ('creation_date', )
        fields = '__all__'
