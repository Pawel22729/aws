import boto3
import sys
db = sys.argv[1]
rds = boto3.client('rds')

try:
    resp = rds.delete_db_instance(
        DBInstanceIdentifier = db,
        SkipFinalSnapshot = True
        )
    print(resp)
except Exception as e:
    print(e)