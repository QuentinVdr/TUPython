from src.moment import Moment


class LangueAnglais:
    def feliciter(self):
        return "Well said !"

    def salutation(self, moment):
        if moment == Moment.MATIN:
            return "Good morning !"
        elif moment == Moment.APRES_MIDI:
            return "Good afternoon !"
        elif moment == Moment.SOIR:
            return "Good evening !"
        elif moment == Moment.NUIT:
            return "Good night !"
        else:
            return "Hello !"

    def revoyure(self):
        return "Good bye"

    def __str__(self):
        return "Anglais"
