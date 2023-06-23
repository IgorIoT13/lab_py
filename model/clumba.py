"""Student Ihor IR-13 """

from model.garden import Garden

class Clumba(Garden):
    """Simulation real clumba"""
    def __init__(self, area, flower):
        super().__init__(area, flower, {"Flower"})

    def has_orchard(self):
        """return status orchard in garden"""

        return True

    def has_vegetable_garden(self):
        """return status vegetable garden in garden"""

        return False
