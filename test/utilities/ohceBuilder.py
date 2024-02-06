from test.utilities.langueStub import LangueStub

from src.OHCE import OHCE


class OHCEBuilder:
    __langue = LangueStub()
    __moment = None

    def build(self):
        return OHCE(self.__langue, self.__moment)

    def init_langue(self, langue):
        self.__langue = langue
        return self

    def init_moment(self, moment):
        self.__moment = moment
        return self
