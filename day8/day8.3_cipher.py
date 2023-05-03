alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encode(plain_text, amount_shift):
    cipher_text = ""
    for ch in plain_text:
        position = alphabet.index(ch)
        new_position = position + amount_shift
        if new_position > 25:
            new_position = new_position - 26
        cipher_text += alphabet[new_position]
    return cipher_text


def decode(cipher_text, amount_shift):
    plain_text = ""
    for ch in cipher_text:
        position = alphabet.index(ch)
        new_position = position - amount_shift
        if new_position < 0:
            new_position = new_position + 26
        plain_text += alphabet[new_position]
    return plain_text


print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')
end_the_session = False
while not end_the_session:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        print(f"Here's the encoded result: {encode(text, shift)}")
    else:
        print(f"Here's the encoded result: {decode(text, shift)}")

    is_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if is_continue == 'no':
        end_the_session = True
