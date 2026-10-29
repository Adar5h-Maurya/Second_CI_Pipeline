def is_pangram(text):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = set(text.lower())
    return alphabet.issubset(letters)