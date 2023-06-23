"""Student Ihor IR-13 """

from abc import ABC, abstractmethod


class Garden(ABC):
    """ Class garden imitate garden"""

    def __init__(self, area: int = 0, flower: int = 0, garden={}):
        """constructor class"""
        self._garden_area = area
        self._garden_number_of_flower = flower
        self._garden_str = garden

    def __iter__(self):
        return self._garden_str

    @staticmethod
    def min_area(min_area, *args):
        input_list = args
        result_str = ""
        result = [garden for garden in input_list if garden._garden_area < min_area]
        for res in result:
            result_str += str(res)

        return result_str

    @abstractmethod
    def has_orchard(self):
        """Method need to return orchard"""

        pass

    @abstractmethod
    def has_vegetable_garden(self):
        """Method need to return vegetable garden"""
        pass

    def plant_flower(self, count):
        """add plant to garden"""
        if count >= 0:
            self._garden_number_of_flower += count

    def remove_flower(self, count):
        """remove flower to garden"""
        if count >= 0:
            self._garden_number_of_flower -= count

    def add_vegetable_region(self, count):
        """add area to garden"""
        if count >= 0:
            self._garden_area += count

    def __str__(self):
        """Print setting object"""
        return f"area: {self._garden_area}, " \
               f"orchard: {self.has_orchard()}, " \
               f"vegetable garden: {self.has_vegetable_garden()}, " \
               f"flower: {self._garden_number_of_flower} " \
               f"List: {self._garden_str} "
