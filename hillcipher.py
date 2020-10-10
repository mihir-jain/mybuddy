# The Hill Cipher
import math
import numpy as np

user = "none"

# Adds filler characters to the plaintext to make its length a multiple of 3
def add_filler_text(text):
    if len(text) % 3:
        return text + " " * (3 - len(text) % 3)
    return text


# Create the matrix P
def string_to_matrix(text):
    return np.array([ord(x) for x in text]).reshape(3, len(text) // 3)


# Given P and K, generate E = K*P
def generate_ciphertext(key, plaintext_matrix):
    return np.matmul(key, plaintext_matrix)


# Given E and K, generate P = K^-1*E
def decrypt_plaintext(key, ciphertext_matrix):
    return np.round(np.matmul(np.linalg.inv(key), ciphertext_matrix))


# Given P, recover the original string
def matrix_to_string(plaintext_matrix):
    ret = ""
    for i in plaintext_matrix:
        for j in i:
            ret += chr(int(j))
    return ret