import boto3

#ami = 'ami-cae150b7' # amazon
ami = 'ami-6276c71f' # centos 7
sg=['sg-071de7a8e9c723c3b']
ec2 = boto3.resource('ec2')
keyName = u'pls-pair'
inst = ec2.create_instances(ImageId=ami, SecurityGroupIds=sg, KeyName=keyName, MinCount=1, MaxCount=1, InstanceType='t2.micro')
print(inst[0].id, inst[0].public_dns_name)

#rsp = ec2.create_instances(
#    ImageId='ami-0922553b7b0369273',
#    InstanceType='t2.micro',
#    KeyName='pls-lunch-config1',
#    MaxCount=1,
#    MinCount=1,
#    NetworkInterfaces=[
#        {
#          'AssociatePublicIpAddress': True,
#          'DeviceIndex': 0,
#          'SubnetId': 'subnet-05878964b12833c54',
#          'Groups': [
#            'sg-08a1d91877efe7af7'
#          ]
#        }
#    ]
#)
