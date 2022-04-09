from .mfa import setup, mfa
import argparse


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='Setup or MFA')
    subparser_setup = subparsers.add_parser('setup', help='setup for MFA via CLI')
    subparser_setup.set_defaults(func=setup)

    subparser_mfa = subparsers.add_parser('mfa', help='Authenticate on the CLI with MFA')
    subparser_mfa.add_argument("aws_profile")
    subparser_mfa.add_argument("token_code")
    subparser_mfa.set_defaults(func=mfa)

    args = parser.parse_args()
    args.func(args)

