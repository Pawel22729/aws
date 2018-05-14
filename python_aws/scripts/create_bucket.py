import boto3
import sys

s3 = boto3.resource('s3')
for bucket_name in sys.argv[1:]:
    try:
        resp = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'eu-west-3'})
    except Exception as e:
        print(e)