import numpy as np
import time
MAXN = 3
def get_result(idx):
	import httplib, urllib, base64
	import re
	import json

	dynamic_time = np.zeros(MAXN)
	static_time = np.zeros(MAXN)
	GET_headers = {
	    # Request headers
	    'Ocp-Apim-Subscription-Key': '',
	}

	GET_params = urllib.urlencode({
	})
	conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
	conn.request("GET", "/video/v1.0/operations/%s?%s" % (idx, GET_params), "", GET_headers)
	response = conn.getresponse()
	data = response.read()
	print data
	parsed_datas = json.loads(data)
	result = parsed_datas['processingResult']
	result = json.loads(result)
	for fragment in result['fragments']:
	    if('events' in fragment):
	    	visited = [0]*MAXN
	    	for event in fragment['events']:
	    		if(event !=[]):
		    		regionId = event[0]['regionId']
		    		if(not(visited[regionId])):
						dynamic_time[regionId] += fragment['duration'];
						visited[regionId] = 1
			static_time += (np.ones(MAXN) - np.array(visited))*fragment['duration']

	    else:
	        static_time += fragment['duration']
	    conn.close()
	print dynamic_time/(dynamic_time + static_time)
	print '\n'
	return dynamic_time/(dynamic_time + static_time)

    # for event in fragment['events']:
    #     if(event):
    #         print event['locations']

f_read = open('idx.txt',"r")
vectors = np.zeros((28,MAXN))
idxes = f_read.read().split('\n')
for idx in idxes:
	if(idx!=''):
		(timeline, idx) = idx.split(' ')
		timeline = int(timeline)
		print idx
		res = get_result(idx)
		print type(timeline),timeline
		vectors[timeline,:] = res
		time.sleep(30)
np.savetxt('motion_vector.txt',np.array(vectors))
