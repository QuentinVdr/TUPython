from utilities.langueStub import LangueStub


class LangueSpy(LangueStub):
    __felicitationsConsultees = False

    def felicitations_consultees(self):
        return self.__felicitationsConsultees

    def féliciter(self):
        self.__felicitationsConsultees = True

    __bonjourConsultees = False

    def bonjour_consultees(self):
        return self.__bonjourConsultees

    def bonjour(self):
        self.__bonjourConsultees = True
