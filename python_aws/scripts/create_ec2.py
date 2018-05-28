import boto3

ami = 'ami-cae150b7'
sg=['sg-071de7a8e9c723c3b']
ec2 = boto3.resource('ec2')
inst = ec2.create_instances(ImageId=ami, SecurityGroupIds=sg, MinCount=1, MaxCount=1, InstanceType='t2.micro')
print(inst[0].id)
