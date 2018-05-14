import boto3
import sys

s3 = boto3.resource('s3')
for bucket_name in sys.argv[1:]:
    bucket = s3.Bucket(bucket_name)
    for key in bucket.objects.all():
        try:
            resp = key.delete()
            print(resp)
        except Exception as e:
            print(e)