import os
import json
from tabulate import tabulate


def get_private_ips(args):
    results = os.popen('aws ec2 describe-instances --query ' +
                       '\'Reservations[*].Instances[*].[Tags[?Key==`Name`].Value[], PrivateIpAddress]\' ' +
                       '--filters Name=instance-state-name,Values=running --output json --region eu-west-1  '
                       '--profile ' + args.aws_profile).read()

    json_res = json.loads(results)
    table_values = []
    for ips in json_res:
        table_values.append([ips[0][0][0], ips[0][1]])

    print(tabulate(table_values, headers=['Name', 'Private IP']))
