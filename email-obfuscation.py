#!/bin/env python

import argparse
import random

parser = argparse.ArgumentParser(
        description='Generate a string to obfuscate your email address')

parser.add_argument('email', type=str, help='email address to obfuscate')
parser.add_argument('-m', '--with-mailto', dest='mailto', action='store_true', 
                    help='Return a string link with mailto obfuscated')

args = parser.parse_args()

# get args.email and transform char in list of ascii code
ascii_char_list = list(ord(char) for char in list(args.email))

# lambda function to transform ascii to html ascii entity
# randomly keep ascii in decimal or return ascii hex
transform = lambda s: random.choice(
                ('&#'+str(s)+';', str(hex(s)).replace('0', '&#', 1)+';'))

#print a string of html entities
print('Email address obfuscated:')
print(''.join(list(map(transform, ascii_char_list))))

if(args.mailto):
    link_mailto = 'mailto:'+args.email
    ascii_char_mailto = list(ord(char) for char in list(link_mailto))
    print('mailto link obfuscated :')
    print(''.join(list(map(transform, ascii_char_mailto))))
