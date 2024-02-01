import os
import unittest

from src.langueAnglais import LangueAnglais
from src.langueFrancais import LangueFrancaise
from test.utilities.langueSpy import LangueSpy
from test.utilities.ohceBuilder import OHCEBuilder


class OHCETest(unittest.TestCase):
    __ohce = OHCEBuilder().build()

    def test_miroir(self):
        # ÉTANT DONNE une chaîne de caractères
        for chaine in ["test", "miroir", "kayak"]:
            with self.subTest(chaine):
                # QUAND je la passe à la fonction miroir
                resultat = self.__ohce.est_palindrome(chaine)
                # ALORS je reçois la chaîne de caractères inversée
                attendu = chaine[::-1]
                self.assertIn(attendu, resultat)

    def test_palindrome_feliciter(self):
        # ÉTANT DONNE la langue de l'utilisateur
        for langue in [LangueFrancaise(), LangueAnglais()]:
            with self.subTest(langue):
                # ÉTANT DONNE une chaîne de caractères
                palindrome = "kayak"
                # QUAND je le passe dans la fonction est palindrome
                resultat = (
                    OHCEBuilder().init_langue(langue).build().est_palindrome(palindrome)
                )
                # ALORS je reçois la chaîne suivie de "Bien dit !"
                attendu = palindrome + os.linesep + langue.feliciter()
                self.assertIn(attendu, resultat)

    def test_non_palindrome(self):
        # ÉTANT DONNE une chaîne de caractères
        langue = LangueSpy()
        non_palindrome = "yakak"
        # QUAND je le passe dans la fonction est palindrome
        self.__ohce.est_palindrome(non_palindrome)
        # ALORS je reçois la chaîne sans félicitation
        self.assertFalse(langue.felicitations_consultees())

    def test_bonjour(self):
        # ÉTANT DONNE une chaîne de caractères
        chaine = "bonjour"
        # QUAND je le passe dans la fonction est palindrome
        resultat = self.__ohce.est_palindrome(chaine)
        # ALORS je reçois "Bonjour" sur la premiere ligne
        premiere_ligne = resultat.split(os.linesep)[0]
        attendu = "Bonjour"
        self.assertEqual(premiere_ligne, attendu)

    def test_au_revoir(self):
        # ÉTANT DONNE une chaîne de caractères
        chaine = "au revoir"
        # QUAND je le passe dans la fonction est palindrome
        resultat = self.__ohce.est_palindrome(chaine)
        # ALORS je reçois "Au revoir" puis la chaîne
        derniere_ligne = resultat.split(os.linesep)[-1]
        attendu = "Au revoir"
        self.assertEqual(derniere_ligne, attendu)
