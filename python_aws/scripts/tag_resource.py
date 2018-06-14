#!/usr/bin/python

import boto3

vol_id = 'vol-0f5e7a234cc0dfc01'
tagK = 'Name'
tagV = 'TestTag'

ec2 = boto3.resource('ec2')
vols = ec2.volumes.all()
for v in vols.all():
    if vol_id in v.id:
        v.create_tags(Tags=[{"Key": tagK, "Value": tagV}])
        print(v)
