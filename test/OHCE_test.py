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
