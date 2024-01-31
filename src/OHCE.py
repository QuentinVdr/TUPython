import os


class OHCE:
    @classmethod
    def est_palindrome(cls, chaine):
        mirror = chaine[::-1]
        response = "Bonjour" + os.linesep + mirror
        if mirror == chaine:
            response += os.linesep + "Bien dit !"
        return response
