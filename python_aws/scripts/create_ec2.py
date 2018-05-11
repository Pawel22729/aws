import boto3

ami = 'ami-cae150b7'
ec2 = boto3.resource('ec2')
inst = ec2.create_instances(ImageId=ami, MinCount=1, MaxCount=1, InstanceType='t2.micro')
print(inst[0].id)
