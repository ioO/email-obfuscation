#!/bin/env python

import argparse

parser = argparse.ArgumentParser(
            description='Generate a string to obfuscate your email address')
parser.add_argument('email', type=str, help='email address to obfuscate')

args = parser.parse_args()

print(args.email)
