#!/usr/bin/python

import boto3
import json

cli = boto3.client('ec2')
sec_groups = cli.describe_security_groups()
sec_groups_names = []
for s in sec_groups['SecurityGroups']:
    sec_groups_names.append(s['GroupName'])
    print(s['GroupName'])

print('First group details')
print(cli.describe_security_groups(
	Filters=[
          {
            'Name': 'group-name',
            'Values': [sec_groups_names[0]]
          }
        ]
      ))
