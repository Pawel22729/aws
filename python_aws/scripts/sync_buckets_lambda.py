#!/usr/bin/python

import boto3
import json
import os

cli = boto3.client('s3')

primary_bucket = cli.list_objects_v2(
    Bucket = os.environ['primary_bucket_name']
)
secondary_bucket = cli.list_objects_v2(
    Bucket = os.environ['failover_bucket_name']
)

def get_keys(bucket_dict):
    '''
        Get the bucket object dict and return the keys
    '''

    keys = []
    try:
        for key_index in bucket_dict['Contents']:
            keys.append(str(key_index['Key']))
    except Exception as e:
        print(e)
    
    return keys

def sync_buckets(primary, secondary):
    '''
        Compare and sync buckets
    '''

    primary_keys = get_keys(primary)
    secondary_keys = get_keys(secondary)

    deprecated_keys = [key for key in secondary_keys if key not in primary_keys]

    return deprecated_keys

def remove_deprecated(deprecated_keys):
    object_list = []
    response = 'Nothing to sync'

    for key in deprecated_keys:
        tmp_dict = {}
        tmp_dict['Key'] = key
        object_list.append(tmp_dict)
    if object_list:
        response = cli.delete_objects(
            Bucket=secondary_bucket['Name'],
            Delete={
                'Objects': object_list
            }
        )
    return json.dumps(response)

def handler(event, lambda_context):
    keys_to_remove = sync_buckets(primary_bucket, secondary_bucket)
    result = remove_deprecated(keys_to_remove)
    print(result)