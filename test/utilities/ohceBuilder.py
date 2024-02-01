from src.OHCE import OHCE
from utilities.langueStub import LangueStub


class OHCEBuilder:
    __langue = LangueStub()

    def build(self):
        return OHCE(self.__langue)

    def init_langue(self, langue):
        self.__langue = langue
        return self
