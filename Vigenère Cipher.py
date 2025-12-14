import random
import tkinter as tk
from tkinter import scrolledtext

alphabets = list("abcdefghijklmnopqrstuvwxyz")

def create_vigenere_table():
    table = []
    for i in range(26):
        row = alphabets[i:] + alphabets[:i]
        table.append(row)
    return table

vigenere_table = create_vigenere_table()

def random_key_generation():
    key = ""
    for i in range(5):
        key += random.choice(alphabets)
    return key

def generate_key(text, key):
    extended_key = ""
    j = 0
    for i in range(len(text)):
        extended_key += key[j % len(key)]
        j += 1
    return extended_key

def encoding(plain_text, key):
    encrypted_text = ""
    key = generate_key(plain_text, key)

    for i in range(len(plain_text)):
        if plain_text[i] in alphabets:
            row = alphabets.index(key[i])
            col = alphabets.index(plain_text[i])
            encrypted_text += vigenere_table[row][col]
        else:
            encrypted_text += plain_text[i]

    return encrypted_text

def decoding(cipher_text, key):
    decoded_text = ""
    key = generate_key(cipher_text, key)

    for i in range(len(cipher_text)):
        if cipher_text[i] in alphabets:
            row = alphabets.index(key[i])
            col = vigenere_table[row].index(cipher_text[i])
            decoded_text += alphabets[col]
        else:
            decoded_text += cipher_text[i]

    return decoded_text

def encode_text():
    global encrypted_text, key

    plain_text = input_text.get("1.0", tk.END).strip().lower()
    if not plain_text:
        return

    key = random_key_generation()
    
    encrypted_text = encoding(plain_text, key)

    encrypted_box.delete("1.0", tk.END)
    encrypted_box.insert(tk.END, encrypted_text)

def decode_text():
    if not encrypted_text:
        return

    decoded_text = decoding(encrypted_text, key)

    decoded_box.delete("1.0", tk.END)
    decoded_box.insert(tk.END, decoded_text)

root = tk.Tk()
root.title("Vigenère Cipher")

tk.Label(root, text="Enter Text:").pack()
input_text = scrolledtext.ScrolledText(root, height=8, width=100)
input_text.pack()

encode_btn = tk.Button(root, text="Encode", command=encode_text)
encode_btn.pack()

tk.Label(root, text="Encrypted Text:").pack()
encrypted_box = scrolledtext.ScrolledText(root, height=8, width=100)
encrypted_box.pack()

decode_btn = tk.Button(root, text="Decode", command=decode_text)
decode_btn.pack()

tk.Label(root, text="Decoded Text:").pack()
decoded_box = scrolledtext.ScrolledText(root, height=8, width=100)
decoded_box.pack()

root.mainloop()
