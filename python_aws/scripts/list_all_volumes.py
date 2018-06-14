#!/usr/bin/python

import boto3

ec2 = boto3.resource('ec2')
volumes = ec2.volumes.all()
for v in volumes:
    print(v)
