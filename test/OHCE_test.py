import os
import unittest

from src.OHCE import OHCE


class OHCETest(unittest.TestCase):
    def test_miroir(self):
        # ÉTANT DONNE une chaîne de caractères
        for chaine in ["test", "miroir"]:
            with self.subTest(chaine):
                # QUAND je la passe à la fonction miroir
                resultat = OHCE.miroir(chaine)
                # ALORS je reçois la chaîne de caractères inversée
                attendu = chaine[::-1]
                self.assertEqual(resultat, attendu)

    def test_palindrome_bien_dit(self):
        # ÉTANT DONNE une chaîne de caractères
        palindrome = "kayak"
        # QUAND je le passe dans la fonction est palindrome
        resultat = OHCE.est_palindrome(palindrome)
        # ALORS je reçois la chaîne suivie de "Bien dit !"
        attendu = palindrome + os.linesep + "Bien dit !"
        self.assertEqual(resultat, attendu)
