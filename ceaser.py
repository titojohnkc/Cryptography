#!/usr/bin/python3
# Ceaser Shift Cypher
# Encrypt and Decrypt Functions

import string
import os
import argparse

#Parse Definition
parser = argparse.ArgumentParser()

parser.add_argument('-e', dest='encode_text')
parser.add_argument('-d', dest='decode_text')

#Generate Alphabet
cypher = []
cypher_text = []
alphabet = list(string.ascii_letters)

def encode_text(plaintext, shift):
	#Find letter in list and record index
	for x in plaintext:
	    cypher.append(alphabet.index(x))
	size = len(cypher)
	count = 0

	while count < size:
	    cypher[count] = cypher[count] + shift
	    count+=1	    

	for x in cypher:
	    if x > size:
	        x = x - 52
	        cypher_text.append(alphabet[x])
	    else:
	        cypher_text.append(alphabet[x])

	return cypher_text


def print_result(plaintext, shift, cypher_text):
	os.system('clear')
	print("Ceaser Cipher Encode Result: ")
	print(f"  Plaintext: {''.join(plaintext)}")
	print(f"      Shift: {shift}")
	print(f"Cipher Text: {''.join(cypher_text)}")




print("Ceaser Cipher")
plaintext = list(input("Enter Your plaintext phrase: "))
shift = int(input("Enter Shift Value: "))

	    
ct = encode_text(plaintext, shift)
print_result(plaintext, shift, ct)




