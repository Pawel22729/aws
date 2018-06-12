import boto3

#ami = 'ami-cae150b7' # amazon
ami = 'ami-6276c71f' # centos 7
sg=['sg-071de7a8e9c723c3b']
ec2 = boto3.resource('ec2')
keyName = u'pls-pair'
inst = ec2.create_instances(ImageId=ami, SecurityGroupIds=sg, KeyName=keyName, MinCount=1, MaxCount=1, InstanceType='t2.micro')
print(inst[0].id, inst[0].public_dns_name)
