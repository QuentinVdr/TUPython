import locale
import time

from src.langueAnglais import LangueAnglais
from src.langueFrancais import LangueFrancaise
from src.moment import Moment
from src.OHCE import OHCE


# get current system hour
def get_system_hour():
    # This will return the current hour
    return int(time.strftime("%H"))


# get moment for init OHCE
def get_moment():
    hour = get_system_hour()
    if 6 <= hour < 12:
        return Moment.MATIN
    elif 12 <= hour < 19:
        return Moment.APRES_MIDI
    elif 19 <= hour < 22:
        return Moment.SOIR
    elif 22 <= hour < 24 or 0 <= hour < 6:
        return Moment.NUIT
    else:
        return Moment.INCONNUE


# get language of user's system
def get_system_language():
    # This will return a string like 'en_US'
    system_lang = locale.getlocale()[0]
    # This will split the string and keep only 'en'
    if system_lang is not None:
        system_lang = system_lang.split("_")[0]
    return system_lang


# get langue for init OHCE
def get_language():
    # set up OHCE with user language
    if get_system_language() == "fr":
        return LangueFrancaise()
    # use english language as default language
    # cause english is international language
    # so user with unsupported language will get english
    else:
        return LangueAnglais()


if __name__ == "__main__":
    language = get_language()
    moment = get_moment()

    ohce = OHCE(langue=language, moment=moment)

    # get text input of user
    user_input = input("Enter a string : ")

    # call the is_palindrome function
    result = ohce.est_palindrome(user_input)

    print(result)
