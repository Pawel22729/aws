#!/usr/bin/env python

import boto3
import sys

sns = boto3.client('sns', region_name='us-east-1')
topic = sys.argv[1]

def unsub_list(new_lst):
    res = sns.list_subscriptions_by_topic(TopicArn=topic)
    remote_lst = {}
    for s in res['Subscriptions']:
        if s['SubscriptionArn'] != 'PendingConfirmation' and s['Protocol'] == 'email':
            remote_lst[s['Endpoint']] = s['SubscriptionArn']
    unsubscribe_lst_arns = [remote_lst[i] for i in remote_lst.keys() if i not in new_lst]
    return unsubscribe_lst_arns

def unsub(who_arns_lst):
    try:
        for arn in who_arns_lst:
            res = sns.unsubscribe(SubscriptionArn=arn)
            return res
    except Exception as e:
        print(e)

support_emails = [
    "example@rmail.com"
]

to_unsub = unsub_list(support_emails)
unsub(to_unsub)
