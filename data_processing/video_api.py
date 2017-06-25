import time
import re
def parse_video(url):
    import httplib, urllib, base64
    import re
    import json


    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    }
    body = "{ 'url': '%s' }" % url
    boxes = [[0.1727,0.3601,0.12,0.1836],[0.2937,0.3706,0.1073,0.2133],[0.6020,0.3846,0.1961,0.2867]]
    string = ''
    for box in boxes:
        string += str(box[0])+','+str(box[1])+';' + str(box[0]+box[3])+','+str(box[1])+';' + str(box[0]+box[2])+','+str(box[1]+box[3])+';' + str(box[0])+','+str(box[1]+box[3])+'|'
    string = string[:-1]
    params = urllib.urlencode({
        # # Request parameters
        'sensitivityLevel': 'low',
        'detectionZones': '%s' % string
    })

    pattern = re.compile(r'operations\/(.*)')
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/video/v1.0/detectmotion?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.getheaders()
    resp = response.read()
    for d in data:
        if(d[0]=='operation-location'):
            data = d[1]
    #data = "https://westus.api.cognitive.microsoft.com/video/v1.0/operations/1a6dad51-fbcc-4d6b-b635-467d1dad2de5"
    print resp
    idx = pattern.search(data)
    if idx:
        idx = idx.group()[11:]
    conn.close()
    return idx
vectors = []
f_idx = open('idx.txt','w')
f_vid = open('mp4_url.txt','r')
data = f_vid.read().split('\n')

for url in data:
    if(url!=''):
        print url
        pattern = re.compile(r'\(\d*\)')
        m = pattern.search(url)
        if(m):
            timeline = int(m.group()[1:-1])
        res = parse_video(url)
        print str(res)+'\n'
        f_idx.write(str(timeline - 1) + ' ' + res+'\n')
        time.sleep(60)








