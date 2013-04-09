from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Conversation(models.Model):
	conversation_title	= models.CharField(max_length= 256,)
	conversation_message	= models.TextField()
	posted_time= models.TimeField(auto_now= True,)
	posted_by= models.ForeignKey(User)
