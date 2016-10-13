import oss2,os
endpoint='http://oss-us-west-1.aliyuncs.com'
auth = oss2.Auth('h9p8vicTD1xAplNn', 'symR186PUptAyQJnF0sKFNeHtGD2jl')
# service=oss2.Service(auth,endpoint)

# for b in oss2.BucketIterator(service):
#     print(b.name)

bucket = oss2.Bucket(auth, endpoint, 'arroyo')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR, '/logo.JPEG'))
bucket.put_object_from_file('remote.JPEG',BASE_DIR+'/logo.JPEG')

