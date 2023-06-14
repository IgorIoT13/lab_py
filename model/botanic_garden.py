"""Student Ihor IR-13 """


from model.garden import Garden


class BotanicGarden(Garden):
    """class need to simulation greenhouse garden"""

    def __init__(self, area: int = 0, flower: int = 0, count_greenhouses: int = 0):
        """Constructor"""

        super().__init__(area, flower)
        self._count_greenhouses = count_greenhouses

    def get_count_greenhouses(self):
        """return greenhouses to use it in code"""
        return self._count_greenhouses

    def has_orchard(self):
        """return status orchard in garden"""

        return True

    def has_vegetable_garden(self):
        """return status vegetable garden in garden"""

        return False

    def __str__(self):
        return super().__str__() + f", greenhouse: {self._count_greenhouses}" + "\n"
