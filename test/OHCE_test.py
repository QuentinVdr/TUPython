import unittest

class OHCETest(unittest.TestCase):
    def test_miroir(self):
      # ÉTANT DONNE une chaîne de caractères
      chaine = "test"
      # QUAND je la passe à la fonction miroir
      result = OHCE.miroir(chaine)
      # ALORS je reçois la chaîne de caractères inversée
      attendu = chaine[::-1]
      self.assertEqual(result, attendu)
