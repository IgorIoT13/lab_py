"""Student Ihor IR-13 """

from model.garden import Garden

class Gorod(Garden):
    """Simulation real GOROD"""

    def has_orchard(self):
        """return status orchard in garden"""

        return True

    def has_vegetable_garden(self):
        """return status vegetable garden in garden"""

        return False
