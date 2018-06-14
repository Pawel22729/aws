#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')
resp = ec2.create_volume(AvailabilityZone="eu-west-3c", Size=1)
print(resp)
