import boto3
import sys

ec2 = boto3.resource('ec2')
for i in sys.argv[1:]:
    inst = ec2.Instance(i)
    resp = inst.terminate()
    print(resp)
