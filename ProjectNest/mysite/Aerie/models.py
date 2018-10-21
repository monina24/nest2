from django.db import models

# Create your models here.
"""
class Task(models.Model);
	task_name = models.CharField(max_length=50)
	due_date = models.DateField()
	assigned_person = models.CharField(max_length=50)
	description = models.CharField(max_length=100)
	currentTask = models.BooleanField()
	finished = models.BooleanField()

class Milestones(models.Model):
	milestone_name = models.CharField(max_length=50)
	tasks = models.ForeignKey(Task, )

"""

class Nest(models.Model):
	
	nest_name = models.CharField(max_length=200)
	description = models.CharField(max_length=500, default="Empty!")
	team_members = models.CharField(max_length=1000)
	progress_percentage = models.IntegerField(default=0)
	is_launched = models.BooleanField(default=True)
	project_type = models.CharField(max_length=100,default="None")
	num_members = models.IntegerField(default=0)
	max_members = models.IntegerField(default=5)
	weekly_committment_hours = models.IntegerField(default=0)


class Account(models.Model):
	account_name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	rating=models.IntegerField(default=1)

class MotivationalQuotes(models.Model):
	quote = models.CharField(max_length=200)