letter_dict = {
    "a": "f", "b": "g", "c": "h", "d": "i", "e": "j",
    "f": "k", "g": "l", "h": "m", "i": "n", "j": "o",
    "k": "p", "l": "q", "m": "r", "n": "s", "o": "t",
    "p": "u", "q": "v", "r": "w", "s": "x", "t": "y",
    "u": "z", "v": "a", "w": "b", "x": "c", "y": "d", "z": "e"
}

sentence = input("Please enter a sentence: ")
sentence = sentence.lower()

encrypted_chars = []
for char in sentence:
    if char in letter_dict:
        encrypted_chars.append(letter_dict[char])
    else:
        encrypted_chars.append(char)
        
encrypted_sentence = "".join(encrypted_chars)
print("The encrypted sentence is: ", encrypted_sentence)

