import locale

from src.langueAnglais import LangueAnglais
from src.langueFrancais import LangueFrancaise
from src.OHCE import OHCE


# get language of user's system
def get_system_language():
    # This will return a string like 'en_US'
    system_lang = locale.getlocale()[0]
    # This will split the string and keep only 'en'
    if system_lang is not None:
        system_lang = system_lang.split("_")[0]
    return system_lang


if __name__ == "__main__":
    # set up OHCE with user language
    if get_system_language() == "fr":
        ohce = OHCE(langue=LangueFrancaise(), moment=None)
    # use english language as default language
    # cause english is international language
    # so user with unsupported language will get english
    else:
        ohce = OHCE(langue=LangueAnglais(), moment=None)

    # get text input of user
    user_input = input("Enter a string : ")

    # call the is_palindrome function
    result = ohce.est_palindrome(user_input)

    print(result)
