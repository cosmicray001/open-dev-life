from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from task.models import Task


class TaskBulkCreateAPIView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            my_title = "brand new task"
            my_short_description = "This is short_description"
            bulk_obj_list = []
            for xl in range(100):
                task_obj = Task(
                    title=my_title + str(xl),
                    short_description=my_short_description
                )
                bulk_obj_list.append(task_obj)
            Task.objects.bulk_create(bulk_obj_list, ignore_conflicts=True)
            return Response({"message": "bulk operation has been executed"}, status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex)
        return Response({"message": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskBulkUpdateAPIView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            task_obj_list = []
            task_queryset = Task.objects.filter(id__iregex='^\d*[13579]$')
            for task in task_queryset:
                task.rating = 1
                task_obj_list.append(task)
            Task.objects.bulk_update(task_obj_list, ['rating'])
            return Response({"message": "bulk operation has been executed"}, status=status.HTTP_200_OK)
        except Exception as ex:
            print(ex)
        return Response({"message": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
