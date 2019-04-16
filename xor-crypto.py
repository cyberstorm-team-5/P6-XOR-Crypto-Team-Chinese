#!/usr/bin/env python2.7
################################################################################
# Authors: Team Chinese (Lane Arnold, Christopher Boquet,
# 	   Christopher Bouton, Darrell Durousseaux, Clay Fonseca,
#	   Rebecca Grantham, Andrew Maurice)
# Class: CSC 442
# Date: 5-1-2019
# Github Repo: https://github.com/cyberstorm-team-5/P6-XOR-Crypto-Team-Chinese
# Description: Program 6: Xor Crypto
#              The Python code will implement the XOR Crypto method by reading
#              a key from a file named "key" in the current directory, along
#              with the plaintext or ciphertext from stdin, and sending the
#              resulting plaintext or ciphertext to stdout.
################################################################################

import os
import sys

###############################MAIN#############################################

#read in plaintext or ciphertext binary file
m = sys.stdin.read()

#retrieve binary data from the "key" binary file in same directory
#as this python file
k = open('key', 'rb').read()

result = ""

#loop through each byte (character) in the message text m and xor with the corresponding
#index from the key k
for i in range(len(m)):
    #key can be shorter than the length of the message, so mod by the length of the key to
    #loop around as needed
    result += chr(ord(m[i]) ^ ord(k[i%len(k)]))

#send resulting text to stdout
print(result)


