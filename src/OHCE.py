import os


class OHCE:
    @classmethod
    def est_palindrome(cls, chaine):
        mirror = chaine[::-1]
        if mirror == chaine:
            return chaine + os.linesep + "Bien dit !"
        return chaine[::-1]
