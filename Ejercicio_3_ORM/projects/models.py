from django.db import models

class Project(models.Model):

    name = models.CharField(max_length=60, null=False, blank=False)
    init_date=models.DateTimeField()
    end_date=models.DateTimeField()

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    description= models.CharField(max_length=250)
    end_date=models.DateTimeField()
    project=models.ForeignKey(Project, on_delete=models.DO_NOTHING)
