import numpy as np
import re
import time
########### Python 2.7 #############
def parse_emotion(url):
    import httplib, urllib, base64
    import json
    from pprint import pprint

    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'xxxxxxxxxxxxxxxxxxxxxxxx',
    }

    params = urllib.urlencode({
    })

    # Replace the example URL below with the URL of the image you want to analyze.
    body = "{ 'url': '%s' }" % url

    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    #   URL below with "westcentralus".
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print data
    parsed_datas = json.loads(data)
    face_locations = []
    emotion_vectors = []
    for data in parsed_datas:
        loc = data['faceRectangle']
        face_locations.append([loc['left'], loc['top'], loc['width'], loc['height']])
        emo = data['scores']
        emotion_vectors.append([emo['anger'],emo['contempt'],emo['disgust'],emo['fear'],emo['happiness'],emo['neutral'],emo['sadness'],emo['surprise']])
    print face_locations
    return emotion_vectors
    conn.close()
f_emo = open('jpg_url.txt','r')
data = f_emo.read().split('\n')
vectors = np.zeros((28,MAXN,8))
res = []
for url in data:
    if(url!=''):
        print url
        if('make' in url):
            No = 0
        elif ('east' in url):
            No = 1
        else:
            No = 2
        last_res = res
        pattern = re.compile(r'\(\d*\)')
        m = pattern.search(url)
        if(m):
            timeline = int(m.group()[1:-1])
        res = parse_emotion(url)
        if(res==[]):
            res = last_res
        print str(res)+'\n'
        vectors[timeline - 1, No, :] = np.array(res[0])
        time.sleep(1)
vectors = vectors.reshape((28,MAXN*8))
np.savetxt('emotion_vector.txt',vectors)
