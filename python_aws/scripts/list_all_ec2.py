import boto3

ec2 = boto3.resource('ec2')
all_inst = ec2.instances.all()

for inst in all_inst:
    print(inst.id, inst.state, inst.public_dns_name)
