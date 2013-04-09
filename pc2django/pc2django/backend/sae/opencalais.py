from pc2django.pc2django.backend.sae import calais
import pprint
import sets


def fetch_calais(contents):
	API_KEY='hpay2cvr76b8e35qa568svcm'
	calais_key = calais.Calais(API_KEY, submitter="python-calais demo")
   
	try:
		result = calais_key.analyze(contents)
		#result.print_summary()
  	except Exception,e:
		print e
		'''
		if hasattr(e, code):
			print e.code
        	if e.code== 500 or e.code==503 or e.code==504:
				return -1
			except ValueError, v:
				print v
				return -1	
		'''
	extracted_tags=[]	
	try:
		extracted_tags+=[tag['name'].lower() for tag in result.socialTag]
	except Exception, e:
		pass

	try:
		extracted_tags+= [topic['categoryName'].lower() for topic in result.topics]
	except Exception, e:
		pass
	try:
		extracted_tags+=[entity['name'].lower() for entity in result.entities]
	except Exception, e:
		print 'Exception in file {0}'.format(filename)
		pass   
	return [extracted_tag for extracted_tag in sets.Set(extracted_tags)]

