from model.garden import Garden


class University_garden(Garden):
    def __init__(self, area: int = 0, flower: int = 0, count_sculpture: int = 0):
        super().__init__(area, flower)
        self.__count_sculpture = count_sculpture

    def get_count_sculpture(self):
        return self.__count_sculpture

    def has_orchard(self):
        return False

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
        return super().__str__() + f", sculpture: {self.__count_sculpture}" + "\n"

