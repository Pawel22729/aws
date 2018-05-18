import boto3

rds = boto3.client('rds')

try:
    resp = rds.create_db_instance(
        DBInstanceIdentifier = 'pabloDB',
        MasterUsername = 'pablo',
        MasterUserPassword = 'pablo123',
        DBInstanceClass = 'db.t2.micro',
        Engine = 'mysql',
        AllocatedStorage = 5
        )
    print(resp)
except Exception as e:
    print(e)
