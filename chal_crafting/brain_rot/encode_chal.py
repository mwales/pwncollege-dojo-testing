#!/usr/bin/env python3

print("#!/usr/bin/exec-suid -- /usr/bin/env python3")
print("import base64")
print("x=\"\"\"")

import base64

chal_script = open("script_with_pictures.py","r")
chal_script_data = chal_script.read()
chal_script.close()

chal_encoded = base64.b64encode(chal_script_data.encode("utf-8"))

rot = [

"rizz", "skibidi", "gyatt", "fanum_tax", "mewing", "looxmax", "only_in_ohio", "baby_gronk", "livvy_dunne", "duke_dennis", "big_yikes",
"bruh", "bussin", "cap", "caught_in_4k", "clapback", "drip", "erm_what_the_sigma", "fit_check", "flex", "girl_boss", "glow_up", "gucci",
"glizzy", "i_oop", "ipad_kid", "not_the_mosquito_again", "main_character", "moots", "metal_pipe_falling", "ok_boomer", "pick-me", "roman_empire",
"secure_the_bag", "simp", "situationship", "slaps", "slay", "stan", "uno_reverse", "vibe_check", "wig",
"grindset", "freddy_fazbear", "a_whole_bunch_of_turbulence",
"the_ocky_way", "axel_in_harlem", "aiden_ross", "goated_with_the_sauce", 
"uncanny", "chungus", "pizza_tower", "poggers", "thug_shaker", "ratio", "all_my_fellas", "gigachad",
"backrooms", "gta_6", "redpilled", "kino", "f_in_the_chat", "360_no_scope", "buggin", "cooked" ]

translator = dict()
index = 0

for i in range(10):
	translator[str(i)] = rot[index]
	index += 1

for i in range(26):
	translator[chr(ord('a') + i)] = rot[index]
	index += 1

for i in range(26):
	translator[chr(ord('A') + i)] = rot[index]
	index += 1

translator['+'] = rot[index]
index += 1
translator['/'] = rot[index]
index += 1
translator['='] = rot[index]
index += 1

super_string = ""
for single_char_code in chal_encoded:
	single_char = chr(single_char_code)
	super_string += translator[single_char]
	super_string += " "

gtf = open("giant_text.txt", "r")
giant_text = gtf.read()
gtf.close()

# Copy the whitespace from the giant text file, but replace all other text with characters from super string

final_string = ""
gtf_index = 0
ss_index = 0
while(ss_index < len(super_string)):
	if ( (giant_text[gtf_index] != ' ') and (giant_text[gtf_index] != '\n') ):
		final_string += super_string[ss_index]
		gtf_index += 1
		ss_index += 1
	else:
		final_string += giant_text[gtf_index]
		gtf_index += 1
	
	if (gtf_index >= len(giant_text)):
		gtf_index = 0

print(final_string)

print("\"\"\"")

#print(super_string)

print(f"t={translator}")
print('y=x.replace(" ","").replace("\\n","")')
print("for a,b in t.items(): y=y.replace(b,a)")
print("exec(base64.b64decode(y))")

