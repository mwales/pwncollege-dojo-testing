#!/usr/bin/env python3

def encode_string(text, seedVal):
	ret_val = ""
	for single_char in text:
		seedVal += 1
		if seedVal > 26:
			seedVal = 0
		if ( ( single_char >= 'A') and (single_char <= 'Z') ):
			new_char_val = ord(single_char) - seedVal
			if (new_char_val < ord('A')):
				new_char_val += 26
			ret_val += chr(new_char_val)
		elif ( ( single_char >= 'a') and (single_char <= 'z') ):
			new_char_val = ord(single_char) - seedVal
			if (new_char_val < ord('a')):
				new_char_val += 26
			ret_val += chr(new_char_val)
		else:
			ret_val += single_char
	return ret_val


def decode_string(text, seedVal):
	print("Unimplemented")

	# Try to make your own decode_string function ...
	# But if you really really need help ...

	# CmRlZiBkZWNvZGVfc3RyaW5nKHRleHQsIHNlZWRWYWwpOgoJcmV0X3ZhbCA9ICIiCglmb3Igc2lu
	# Z2xlX2NoYXIgaW4gdGV4dDoKCQlpZiBzZWVkVmFsID4gMjY6CgkJCXNlZWRWYWwgPSAwCgkJaWYg
	# KCAoIHNpbmdsZV9jaGFyID49ICdBJykgYW5kIChzaW5nbGVfY2hhciA8PSAnWicpICk6CgkJCW5l
	# d19jaGFyX3ZhbCA9IG9yZChzaW5nbGVfY2hhcikgKyBzZWVkVmFsCgkJCWlmIChuZXdfY2hhcl92
	# YWwgPiBvcmQoJ1onKSk6CgkJCQluZXdfY2hhcl92YWwgLT0gMjYKCQkJcmV0X3ZhbCArPSBjaHIo
	# bmV3X2NoYXJfdmFsKQoJCWVsaWYgKCAoIHNpbmdsZV9jaGFyID49ICdhJykgYW5kIChzaW5nbGVf
	# Y2hhciA8PSAneicpICk6CgkJCSMgISEhISEhISEhCgkJCSMgV2hvb3BzLCBmb3Jnb3QgdG8gZmls
	# bCB0aGlzIHBhcnQgb3V0LCBJIGd1ZXNzIHlvdSB3aWxsIGhhdmUgdG8KCQkJIyAhISEhISEhISEK
	# CQllbHNlOgoJCQlyZXRfdmFsICs9IHNpbmdsZV9jaGFyCglyZXR1cm4gcmV0X3ZhbAoK

def decrypt(text1, one_time_pad):
	how_many_chars = min(len(text1), len(one_time_pad))

	ret_val = ""
	for i in range(how_many_chars):
		text1val = ord(text1[i])
		ret_val += chr(one_time_pad[i] ^ text1val)
	return ret_val

def main():
	joke="Why did the guy with all the rizz ask Livvy to the function?"
	print(joke)

	user_answer = input()

	user_answer_encode_compare = "Gifcvse fb fhxo xtf htln dgx ewtsim xjy aw txra'e fiutf iwnbld qdz usx. Ggdlsppa B qq cao. lcugmd iok"
	user_answer_encode = encode_string(user_answer, 20)

	if (user_answer_encode == user_answer_encode_compare):
		print("Great job!")

		ff = open("/flag.txt","r")
		flag = ff.read()
		ff.close()

		print(f"Here is your flag: {flag}")
	else:
		print("Phanum tax time")

main()

