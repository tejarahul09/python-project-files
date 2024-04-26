alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plain_text , shift_amount):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_postioin = position + shift_amount
        new_letter = alphabet[new_postioin]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
def decrpt(cipher_text , shift_amount):
    plain_text = ""
    for letter in text:
        postion = alphabet.index(letter)
        new_postion = postion - shift_amount
        plain_text += alphabet[new_postion]
        print(f"the ciphered code is decode : {plain_text}")
if direction == "encode":
    encrypt(plain_text = text , shift_amount=shift)
elif direction == "decode":
    decrpt(cipher_text=text , shift_amount=shift)