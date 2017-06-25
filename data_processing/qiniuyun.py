from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os
import os.path
access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
q = Auth(access_key, secret_key)

bucket_name = 'xxxxxxxxxx'




rootdir = './office'
for parent,dirnames,filenames in os.walk(rootdir):

	for filename in filenames:   
		full_name = os.path.join(parent,filename)
		localfile = full_name
		key = full_name[1:]
		token = q.upload_token(bucket_name, key, 3600)
		ret, info = put_file(token, key, localfile)
		print(info)
		assert ret['key'] == key
		assert ret['hash'] == etag(localfile)
