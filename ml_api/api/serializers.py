from rest_framework import serializers
from .models import Task, Config
import json


class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ['version', 'description', 'hyperparameters']

    def to_representation(self, instance):
        rep = super(ConfigSerializer, self).to_representation(instance)
        rep['hyperparameters'] = json.loads(rep.get('hyperparameters'))
        return rep


class TaskSerializer(serializers.ModelSerializer):
    configuration = ConfigSerializer(many=False, read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
