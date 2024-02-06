from src.moment import Moment


class LangueFrancaise:
    def feliciter(self):
        return "Bien dit !"

    def salutation(self, moment):
        if moment == Moment.MATIN:
            return "Bon matin !"
        elif moment == Moment.APRES_MIDI:
            return "Bon après-midi !"
        elif moment == Moment.SOIR:
            return "Bonsoir !"
        elif moment == Moment.NUIT:
            return "Bonne nuit !"
        else:
            return "Salut !"

    def revoyure(self, moment):
        if moment == Moment.MATIN:
            return "Bonne journée"
        elif moment == Moment.APRES_MIDI:
            return "Bonne fin de journée"
        elif moment == Moment.SOIR:
            return "Bonne soirée"
        elif moment == Moment.NUIT:
            return "Bonne nuit"
        else:
            return "Au revoir"

    def __str__(self):
        return "Française"
