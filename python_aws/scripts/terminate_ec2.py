import boto3
import sys

ec2 = boto3.resource('ec2')
inst = ec2.Instance(sys.argv[1])
resp = inst.terminate()
print(resp)