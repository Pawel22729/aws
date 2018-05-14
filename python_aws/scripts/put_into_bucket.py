import boto3
import sys

s3 = boto3.resource('s3')
bucket_name = sys.argv[1]
object_name = sys.argv[2]
try:
    resp = s3.Object(bucket_name, object_name).put(Body=open(object_name, 'rb'))
    print(resp)
except Exception as e:
    print(e)