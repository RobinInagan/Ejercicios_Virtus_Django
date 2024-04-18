from django.shortcuts import render

# Other Modules
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
#Self Modules
from .models import *
from .serializers import *
#Utils
from datetime import datetime

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializerModel

class TasksViewSet(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializerModel

class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializerModel

class ProjectAPIView(APIView):
    
    def get(self,request):
        projects = Project.objects.all()
        
        # data = [
        #     {
        #         "id": project.id,
        #         "name": project.name,
        #     }
        #     for project in projects
        # ]

        serializer = ProjectSerializer(projects,many=True)
        return Response(serializer.data)
    
    def post(self,request):

        project = Project()
        # project.name = request.data.get("name","")
        # project.init_date = datetime.now()
        # end_date = request.data.get("end_date","")
        # project.end_date = datetime.strptime(end_date,'%d-%m-%YT%H:%M:%S')
        # project.save()
        serializer = ProjectSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})

    def delete(self,request):
        id = request.data.get("id")
        project = Project.objects.get(id=id)
        print(project)
        project.delete()
        return Response({})
    
    def patch(self,request):
        id = request.data.get("id")
        project = Project.objects.get(id=id)
        
        project.name=request.data.get("name",project.name)
        project.save()
        return Response({
            "id": project.id,
            "name": project.name
        })
    
class TaskAPIView(APIView):

    def get(self,request):
        tasks = Tasks.objects.all()
        
        data = [
            {
                "id": task.id,
                "description": task.description,
                "priority" : task.priority 
            }
            for task in tasks
        ]

        return Response(data)
    
    def post(self,request):

        project_name = Project()
        project_name.name = request.data.get("project","")
        priority = request.data.get("priority","")

        try:
            project = Project.objects.get(name=project_name)
        except Project.DoesNotExist:
            return Response({"error": "El proyecto especificado no existe."}, status=status.HTTP_400_BAD_REQUEST)
        if priority not in [choice[0] for choice in Tasks.priority_choices]:
            return Response({"error": "La prioridad especificada no es válida."}, status=status.HTTP_400_BAD_REQUEST)
        
        task = Tasks()
        task.description = request.data.get("description","")
        end_date = request.data.get("end_date","")
        task.end_date = datetime.strptime(end_date,'%d-%m-%YT%H:%M:%S')
        task.project = project
        task.priority = priority
        task.save()
        
        return Response()
    
    def delete(self,request):
        id = request.data.get("id")
        task = Tasks.objects.get(id=id)
        print(task)
        task.delete()
        return Response()
    
    def patch(self,request):
        id = request.data.get("id")
        task = Tasks.objects.get(id=id)
        task.description = request.data.get("description",task.description)
        task.save()
        return Response({
            "id" : task.id,
            "description" : task.description
        })