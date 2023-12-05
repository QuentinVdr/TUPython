import unittest
from datetime import datetime

# Prompts the user to choose a language between fr and en
def choose_language():
    while True:
        user_input = input("Choose your language (fr/en): ").lower()
        if user_input in ["fr", "en"]:
            return user_input
        else:
            print("Invalid choice. Please enter 'fr' for French or 'en' for English.")

def greeting(lang):
    current_hour = datetime.now().hour
    if lang == "en":
        if 5 <= current_hour < 12:
            print("morning")
        elif 12 <= current_hour < 18:
            print("afternoon")
        else:
            print("evening")
    else:
        if 5 <= current_hour < 16:
            print("bonjour")
        elif 16 <= current_hour < 22:
            print("bonsoir")
        else:
            print("bienvenue")

# Reverses the given string.
def reverse_string(input_string):
    return input_string[::-1]

class TestReverseStringFunction(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")
        self.assertEqual(reverse_string("racecar"), "racecar")

if __name__ == '__main__':
    chosen_language = choose_language()
    greeting(chosen_language)
