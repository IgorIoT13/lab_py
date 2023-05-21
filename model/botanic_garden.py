from model.garden import Garden

class Botanic_garden(Garden):
    def __init__(self, area: int = 0, flower: int = 0, count_greenhouses: int = 0):
        super().__init__(area, flower)
        self.__count_greenhouses = count_greenhouses

    def get_count_greenhouses(self):
        return self.__count_greenhouses

    def has_orchard(self):
        return True

    def has_vegetable_garden(self):
        return False

    @staticmethod
    def plant_flower(flower):
        super().plant_flower(flower)

    @staticmethod
    def remove_flower(count):
        super().remove_flower(count)

    @staticmethod
    def add_vegetable_region(count):
        """add area to garden"""
        super().add_vegetable_region(count)

    def __str__(self):
        return super().__str__() + f", greenhouse: {self.__count_greenhouses}" + "\n"

