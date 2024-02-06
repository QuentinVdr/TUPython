import os


class OHCE:
    def __init__(self, langue, moment):
        self.__moment = moment
        self.__langue = langue

    def est_palindrome(self, chaine):
        mirror = chaine[::-1]
        response = self.__langue.salutation(self.__moment) + os.linesep + mirror
        if mirror == chaine:
            response += os.linesep + self.__langue.feliciter()
        response += os.linesep + self.__langue.revoyure(self.__moment)
        return response
