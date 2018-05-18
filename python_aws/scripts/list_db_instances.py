import boto3

rds = boto3.client('rds')

try:
    dbs = rds.describe_db_instances()
    for db in dbs['DBInstances']:
        print(db)
except Exception as e:
    print(e)