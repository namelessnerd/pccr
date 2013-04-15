from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from common.connectors.Mongo import MongoConnector as mc
from backend.sae import opencalais
# Create your models here.

class Project(models.Model):
    project_title=models.CharField(max_length= 256,)
    project_url=models.URLField()
    project_description=models.TextField()
    posted_time= models.TimeField(auto_now= True,)
    posted_by= models.ForeignKey(User)

    def analyze_and_save(self):
        try:
            res= opencalais.fetch_calais(self.project_description)
            if res:
                mongo_c= mc(db='pccr')
                mongo_c.update({'pid':self.id},
                            {'project_title':self.project_title,
                             'project_description':self.project_description,
                             'project_url':self.project_url,
                             'project_tags':res,
                             'posted_by':self.posted_by.id,
                             'pid':self.id,
                             }, collection='pccr_project')
                mongo_c.close_connection()
        except Exception, e:
            print e
            pass

    @staticmethod
    def get_tags(project_id):
        mongo_c= mc(db='pccr')
        res= mongo_c.find_one({'pid':int(project_id)},
                                fields=('project_tags',),
                                collection='pccr_project')
        mongo_c.close_connection()
        try:
            return res[0]['project_tags']
        except Exception, e:
            print e
            return {}

class Researcher(models.Model):

    @staticmethod
    def get_details(user):
        mongo_c= mc(db='pccr')
        res= mongo_c.find_one({'uid':user.id},collection='pccr_researcher')
        mongo_c.close_connection()
        try:
            #return {key: value for key, value in res[0].iteritems() if key!='_id' and key!='uid'}
            return {key: value for key, value in res[0].iteritems()}
        except:
            return {}

    def save(self, name, email, institution, user):
        mongo_c= mc(db='pccr')
        mongo_c.update({'uid':user.id},{'name':name, 'email':email, 'institution':institution,'uid':user.id}, collection='pccr_researcher')
        mongo_c.close_connection()

def analyze_and_save(sender, **kwargs):
    try:
        res= opencalais.fetch_calais(sender.project_description)
        if res:
            mongo_c= mc(db='pccr')
            mongo_c.update({'pid':sender.id},
                        {'project_title':sender.project_title,
                         'project_description':sender.project_description,
                         'project_url':sender.project_url,
                         'project_tags':res,
                         'pid':sender.id,
                         }, collection='pccr_researcher')
            mongo_c.close_connection()
    except Exception, e:
        print e
        pass
#post_save.connect(analyze_and_save, sender= Project)
