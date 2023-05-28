"""Student Ihor IR-13 """

from model.garden import Garden


class UniversityGarden(Garden):
    """Simulation real university garden"""

    def __init__(self, area: int = 0, flower: int = 0, count_sculpture: int = 0):
        """Constructor"""

        super().__init__(area, flower)
        self._count_sculpture = count_sculpture

    def get_count_sculpture(self):
        """return greenhouses to use it in code"""

        return self.__count_sculpture

    def has_orchard(self):
        """return status orchard in garden"""

        return False

    def has_vegetable_garden(self):
        """return status vegetable garden in garden"""

        return False

    def __str__(self):
        return super().__str__() + f", sculpture: {self._count_sculpture}" + "\n"
