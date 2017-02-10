import string

alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
    index = alphabet.find(letter.lower())
    return index

def rotate_character(char, rot):
    encrypted=""
    rot = int(rot)
    if char==chr(32):
        encrypted=chr(32)
    elif char in string.digits:
        encrypted=char
    elif char in string.punctuation:
        encrypted=char
    else:
        index = alphabet_position(char.lower()) + rot
        if index >= len(alphabet):
            index=index%len(alphabet)
        encrypted = alphabet[index]
        if char in string.ascii_uppercase:
            encrypted=encrypted.upper()
    return encrypted

def encrypt(text,rot):
    encrypted=""
    for char in text:
        encrypted = encrypted + rotate_character(char,rot)
    return encrypted