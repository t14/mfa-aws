import os
import json
import configparser
from pathlib import Path

def setup(args):
    aws_profile = input("Enter the profile name of the AWS account that requires MFA: ")
    mfa_arn = input("Enter the ARN of the mfa device: ")
    aws_config_dir = os.path.expanduser("~") + '/.aws'

    config = configparser.ConfigParser()
    config.read(getConfigPath())
    config.add_section(aws_profile)
    config.set(aws_profile, 'MFA_ARN', mfa_arn)
    config.set(aws_profile, 'AWS_PROFILE', aws_profile)

    with open(getConfigPath(), 'w') as configfile:
        config.write(configfile)

    aws_credentials = configparser.ConfigParser()
    aws_credentials.read(aws_config_dir + '/credentials')
    aws_credentials.add_section(aws_profile + '-mfa')

    with open(aws_config_dir + '/credentials', 'w') as aws_credentials_file:
        aws_credentials.write(aws_credentials_file)

    print("Setup complete")


def mfa(args):
    config = configparser.ConfigParser()
    config.read(getConfigPath())
    mfa_device_arn = config[args.aws_profile]['MFA_ARN']
    aws_profile = config[args.aws_profile]['AWS_PROFILE']

    aws_credentials = configparser.ConfigParser()
    stream = os.popen("aws sts get-session-token --serial-number " + mfa_device_arn + " --token-code " +
                      args.token_code + " --profile " + aws_profile)

    output = stream.read()
    credentials = json.loads(output)

    aws_credentials.set(aws_profile + "-mfa", 'aws_access_key_id', credentials['Credentials']['AccessKeyId'])
    aws_credentials.set(aws_profile + "-mfa", 'aws_secret_access_key', credentials['Credentials']['SecretAccessKey'])
    aws_credentials.set(aws_profile + "-mfa", 'aws_session_token', credentials['Credentials']['SessionToken'])

    with open('/Users/jegedtw1/.aws/credentials', 'w') as credentialfile:
        aws_credentials.write(credentialfile)

    print('Authentication complete. Token will expire at ' + credentials['Credentials']['Expiration'])

def getConfigPath():
    home_path = os.path.expanduser("~")
    if not Path(home_path + '/.aws-tools').exists():
        os.makedirs(home_path + '/.aws-tools')
    return home_path + '/.aws-tools/config.cfg'
