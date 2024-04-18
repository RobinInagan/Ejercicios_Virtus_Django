import datetime
from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=60)
    init_date = serializers.DateTimeField(required=False)
    end_date = serializers.DateTimeField()

    def validate_name(self,value):
        if "robinson" in value:
            raise serializers.ValidationError('the name robinson cant be in the project name')
        return value

    def validate(self, attrs):
        # if attrs.get("end_date") < datetime.now():
        #     raise serializers.ValidationError('La fecha de finalización no pude ser menor a la de inicio (fecha y hora actual)')
        return super().validate(attrs)



    def create(self, validated_data):

        Project(**validated_data).save()

        return self.data
    
class ProjectSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class TaskSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class CommentsSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

    def validate_content(self,value):
        ForbiddenWords = ['puto','marica','hijueputa','malparido','mierda']
        for word in ForbiddenWords:
            if word in value:
                raise serializers.ValidationError('The content of the comment cant include bad words')
        return value