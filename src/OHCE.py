import os


class OHCE:
    def __init__(self, langue):
        self.__langue = langue

    def est_palindrome(self, chaine):
        mirror = chaine[::-1]
        response = self.__langue.salutation() + os.linesep + mirror
        if mirror == chaine:
            response += os.linesep + self.__langue.feliciter()
        response += os.linesep + "Au revoir"
        return response
