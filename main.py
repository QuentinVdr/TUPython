from src.langueAnglais import LangueAnglais
from src.OHCE import OHCE

if __name__ == "__main__":
    ohce = OHCE(langue=LangueAnglais(), moment=None)

    # get text input of user
    user_input = input("Enter a string : ")

    # call the is_palindrome function
    result = ohce.est_palindrome(user_input)

    print(result)
