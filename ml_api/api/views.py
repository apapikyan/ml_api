from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from functools import reduce
import json
from .models import Task, Config
from .serializers import TaskSerializer, ConfigSerializer


mandatory_setting = ['appVersion', 'description']
mandatory_params = ['bootstrap', 'criterion', 'maxFeatures', 'minImpurityDecrease', 'nEstimators', 'nJobs']


class TasksViewSet(viewsets.ModelViewSet):
    """
    The class is responsible for all the CRUD operations for Tasks
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        settings = data.get('generalSettings')

        if not all(s in settings for s in mandatory_setting):
            return Response({'Error': 'Missing mandatory settings'}, status=status.HTTP_401_UNAUTHORIZED)

        parameters = data.get('hyperparameters')
        if not all(s in parameters for s in mandatory_params):
            return Response({'Error': 'Missing mandatory params'}, status=status.HTTP_401_UNAUTHORIZED)

        # get rid of none values
        parameters = {k: v for k, v in parameters.items() if v is not None}
        # sort params by keys and then convert to list
        params = list(reduce(lambda x, y: x + y, sorted(parameters.items())))
        params_json = json.dumps(params)

        configs = Config.objects.filter(version=settings.get('appVersion'), description=settings.get('description'),
                                        hyperparameters=params_json)
        if configs.exists():
            return Response({'Error': 'Duplicate Values'}, status=status.HTTP_409_CONFLICT)

        config = Config(version=settings.get('appVersion'), description=settings.get('description'),
                        hyperparameters=params_json)
        config.save()
        task = Task(configuration=config)
        task.save()
        return Response({"id": task.id}, status=status.HTTP_201_CREATED)
