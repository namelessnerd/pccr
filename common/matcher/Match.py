import sys

sys.path.append('/home/karthik/pccr-env/pccr')
sys.path.append('/home/karthik/pccr-env/pccr/pc2django')
sys.path.append('/home/karthik/pccr-env/pccr/pc2django/pc2django')
sys.path.append('/home/karthik/pccr-env/pccr/me_med')
sys.path.append('/home/karthik/pccr-env/pccr/me_med/me_med')
#import os
#os.environ['DJANGO_SETTINGS_MODULE']= 'settings'

from common.connectors.Mongo import MongoConnector as mc
from pccrportal.models import Project
import operator



def match(pid):
	#django query to find all patients who have one or more entities matching
	# researcher project profile
	m= mc(db='pccr')	
	tags= Project.get_tags(pid)
	res= m.find({'tags':{'$in':tags}}, collection='patient_tags_new')
	user_tag_set={}
	for r in res:
		try:
			user_tag_set[str(r['username'])].append(r['tags'])
		except:
			user_tag_set[str(r['username'])]=[r['tags']]
	'''
		try:
			user_tag_set[str(r['username'])].append(r[tags])
		except:
			user_tag_set[str(r['username'])]= []
	'''
	user_score_set={}
	tags= frozenset(tags)
	for user, user_tags in user_tag_set.iteritems():
		for user_tag in user_tags:
			try:
				user_score_set[user]+= len(set(user_tag).intersection(tags))
			except:
				user_score_set[user]= len(set(user_tag).intersection(tags))
	

	sorted_user_scores= sorted(user_score_set.iteritems(), key=
			operator.itemgetter(1))
	return sorted_user_scores[-5:]

match(1)
