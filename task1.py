import itertools
import string
from nltk.corpus import words

# Load English words for dictionary check
dictionary = set(words.words())

def decrypt(text, key_mapping):
    decrypted_text = "".join(key_mapping.get(char, char) for char in text)
    return decrypted_text

def is_probable_english(text):
    words_in_text = text.split()
    count = sum(1 for word in words_in_text if word.lower() in dictionary)
    return count / max(len(words_in_text), 1) > 0.5  # Threshold for probable English text

def brute_force_attack(ciphertext):
    alphabet = string.ascii_uppercase
    for perm in itertools.permutations(alphabet):
        key_mapping = dict(zip(alphabet, perm))
        decrypted_text = decrypt(ciphertext, key_mapping)
        
        if is_probable_english(decrypted_text):
            print("Possible Decryption:", decrypted_text)
            break  # Stop at the first valid result

# Example usage:
ciphertext = "JLAP FJHERFJL OFE"  # Example encrypted text
brute_force_attack(ciphertext)
