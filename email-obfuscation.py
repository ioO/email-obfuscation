#!/bin/env python

import argparse

parser = argparse.ArgumentParser(
            description='Generate a string to obfuscate your email address')
parser.add_argument('email', type=str, help='email address to obfuscate')

args = parser.parse_args()

# get args.email and transform char in list of ascii code
ascii_char_list = list(ord(char) for char in list(args.email))

print(ascii_char_list)
