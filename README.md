Based on https://aws.amazon.com/premiumsupport/knowledge-center/authenticate-mfa-cli/ This script automates the process of authenticating with a Multi Factor Authentication (MFA) token when using the
AWS Command Line Interface (CLI)

# Getting started

```sh
brew install python3
sudo python3 setup.py install
```
You should now be able to run this script from anywhere in the terminal

```sh
# Now try
mfa-aws -h
```

## Available scripts
Multi factor auth for cli - automates MFA on the CLI
When using it for the first time run the setup command
```sh
mfa-aws setup
```

Anytime you need mfa auth on the cli you can run the command like below
```sh
mfa-aws mfa <aws-profile> <mfa-token-code>
```
Once you have successfully authenticated with the above command run your aws commands with the `--profile`
flag prefixing your aws profile name with `-mfa` for example

```sh
aws s3 ls --profile <aws-profile>-mfa
```

## Prerequisite
Make sure you have installed AWS CLI

