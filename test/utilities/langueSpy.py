from utilities.langueStub import LangueStub


class LangueSpy(LangueStub):
    __felicitationsConsultees = False

    def félicitationsConsultées(self):
        return self.__felicitationsConsultees

    def féliciter(self):
        self.__felicitationsConsultees = True
