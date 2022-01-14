# Getting started
This is a bunch of scripts to help with automating some of the manual aspects of working with our aws platform
It is written in python 3, chances are that your standard mac build is running python 2 so follow the steps below to
get started

```sh
brew install python3
sudo python3 setup.py install
```
You should now be able to run these script from anywhere in the terminal
```sh
# Now try
aws-tools -h
```

## Available scripts
Multi factor auth for cli - automates MFA on the CLI
When using it for the first time run the setup command
```sh
aws-tools setup
```

Anytime you need mfa auth on the cli you can run the command like below
```sh
aws-tools mfa <aws-profile> <mfa-token-code>
```

#### Dev setup
If you want to make changes to any of this code follow the steps below to set up a dev envioronment

```sh
python3 -m venv [this directory]
```

#### Start your virtual environment
```sh
cd [this directory]
source bin/activate
```

You can now make changes to the source code and test them out without impacting the already installed code

#### Deactivating your virtual environment
Once you finished working on your project, it’s a good habit to deactivate its venv. Without deactivating it,
all other Python code you execute will also run inside of it
```sh
cd [this directory]
deactivate
```

#### Deleting your virtual environment
```sh
cd [this directory]
deactivate
rm -r venv (assuming your virtual env name is venv)
```
