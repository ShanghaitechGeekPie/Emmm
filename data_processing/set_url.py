import os
import os.path
f_jpg = open('jpg_url.txt','w')
f_mp4 = open('mp4_url.txt','w')
rootdir = './office'
name = 'http://xxxxxxx.bkt.gdipper.com/'
for parent,dirnames,filenames in os.walk(rootdir):

	for filename in filenames:   
		full_name = os.path.join(parent,filename)
		localfile = full_name
		key = full_name[1:]
		if('jpg' in key):
			f_jpg.write(name+key+'\n')
		else:
			f_mp4.write(name+key+'\n')
f_jpg.close()
f_mp4.close()
