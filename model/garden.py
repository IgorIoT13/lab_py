"""Student Ihor IR-13 """


from abc import ABC, abstractmethod
class Garden(ABC):
    """ Class garden imitate garden"""

    def __init__(self, area: int = 0, flower: int = 0):
        """constructor class"""
        self.__garden_area = area
        self.__garden_number_of_flower = flower

    @abstractmethod
    def has_orchard(self):
        pass

    @abstractmethod
    def has_vegetable_garden(self):
        pass

    def plant_flower(self, count):
        """add plant to garden"""
        if count >= 0:
            self.__garden_number_of_flower += count

    def remove_flower(self, count):
        """remove flower to garden"""
        if count >= 0:
            self.__garden_number_of_flower -= count

    def add_vegetable_region(self, count):
        """add area to garden"""
        if count >= 0:
            self.__garden_area += count

    def __str__(self):
        """Print setting object"""
        return f"area: {self.__garden_area}, " \
               f"orchard: {self.has_orchard()}, " \
               f"vegetable garden: {self.has_vegetable_garden()}, " \
               f"flower: {self.__garden_number_of_flower}"
