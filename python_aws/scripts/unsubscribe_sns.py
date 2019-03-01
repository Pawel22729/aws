#!/usr/bin/env python

import boto3
import sys
import argparse

sns = boto3.client('sns', region_name='us-east-1')

def unsub_list(new_lst, topic):
    """Return the list of SNS ARNs to be unsubscribed."""
    res = sns.list_subscriptions_by_topic(TopicArn=topic)
    remote_lst = {}
    for s in res['Subscriptions']:
        if s['SubscriptionArn'] != 'PendingConfirmation' and s['Protocol'] == 'email':
            remote_lst[s['Endpoint']] = s['SubscriptionArn']
    unsubscribe_lst_arns = [remote_lst[i] for i in remote_lst.keys() if i not in new_lst]
    return unsubscribe_lst_arns

def unsub(who_arns_lst):
    """Unsubscribing SNS ARNS passed as list of ARNs."""
    if len(who_arns_lst) == 0:
        print('Nothing to do')
    else:
        try:
            for arn in who_arns_lst:
                res = sns.unsubscribe(SubscriptionArn=arn)
                print('Unsubscribed: ', arn)
                print('HTTPStatusCode: ', res['ResponseMetadata']['HTTPStatusCode'])
        except Exception as e:
            print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topic', required=True, help='topic sns arn')
    parser.add_argument('-s', '--subscribers', required=True, help='the list of subscribers')

    args = parser.parse_args()
    who_to_unsub = unsub_list(args.subscribers, args.topic)
    unsub(who_to_unsub)
