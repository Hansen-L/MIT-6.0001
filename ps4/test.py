import string


letter_to_number_dict={}
number_to_letter_dict={}
num = 1
shift = 2
#First make a dictionary that holds the default letter-number correspondence
for char in string.ascii_lowercase:
    letter_to_number_dict[char] = num
    number_to_letter_dict[num] = char
    num = num + 1
for char in string.ascii_uppercase:
    letter_to_number_dict[char] = num
    number_to_letter_dict[num] = char
    num = num + 1
    
#Now create a new dictionary with letter-shifted letter correspondence by referencing other dict with a shift    



encryption_dict={}

for char in string.ascii_lowercase:
    unshifted_number = letter_to_number_dict[char]
    if unshifted_number <= 26-shift:
        shifted_number = unshifted_number+shift 
    else:
        shifted_number = unshifted_number+shift-26
    encryption_dict[char]=number_to_letter_dict[shifted_number]

for char in string.ascii_uppercase:
    unshifted_number = letter_to_number_dict[char]
    if unshifted_number <= 52-shift:
        shifted_number = unshifted_number+shift
    else:
        shifted_number = unshifted_number+shift-26
    encryption_dict[char]=number_to_letter_dict[shifted_number]
    
    