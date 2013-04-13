from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
	project_title=models.CharField(max_length= 256,)
	project_url=models.URLField()
	project_description=models.TextField()
	posted_time= models.TimeField(auto_now= True,)
	posted_by= models.ForeignKey(User)
