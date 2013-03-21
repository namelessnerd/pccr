import calais
from calais import Calais
import pprint

def fetch_calais():
	API_KEY='hpay2cvr76b8e35qa568svcm'
	calais = Calais(API_KEY, submitter="python-calais demo")
	#contents= 'Epilepsy is the most common serious chronic neurological disease in childhood, and localization related epilepsy (LRE) is the largest pediatric epilepsy group in aggregate. This study will determine changes in cognitive abilities (eg, attention) associated with three of the most common medications used to treat pediatric LRE. Children who are newly diagnosed with LRE by their treating physicians and are between 6 and 12 years of age will be randomized to levetiracetam, lamotrigine, or oxcarbazepine.'
	contents= 'Health insurance is important for children. Public insurance programs are available to many children, but some families report confusion about how to get and keep this insurance. Community health clinics can help families get and keep health insurance for their children.We will work with families, policy makers, and community healthcare providers to develop and test new computer tools to help people in the clinic find pediatric patients in need of insurance and communicate with their families about public insurance programs.'
	result = calais.analyze(contents)
	open_calais_extract={'topics':[], 'entities':[]}
	try:
		map(lambda topic: open_calais_extract['topics'].append({'cat_name':topic['categoryName'], 'rel_score':topic['score']}) if topic['score'] and topic['score']>=0.2 else False, result.topics)
	except Exception, e:
		pass
	try:
		rel_entities= open_calais_extract['entities']
		map(lambda entity: rel_entities.append({'name':entity['name'],'type':entity['_type'],'rel_score':entity['relevance']}) if entity['relevance'] and entity['relevance']>=0.1 else entity['name'], result.entities)
	except Exception, e:
		pass   
	pprint.pprint(open_calais_extract)
	return 1

def main():
	fetch_calais()
     	 

if __name__=='__main__':
	main()
