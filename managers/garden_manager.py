"""Student Ihor IR-13 """
from model.garden import Garden


class GardenManager:
    """Manage all object class Garden"""

    def __init__(self):
        """Constructor"""
        self.__gardens_list_objects = []

    def add_to_garden(self, obj_garden: Garden):
        """Need to add object to list"""
        self.__gardens_list_objects.append(obj_garden)

    def zip(self):
        result = ""
        garden_list = [garden.min_area(1, garden) for garden in self.__gardens_list_objects]

        for garden in garden_list:
            result += str(garden) + "\n"

        return result

    def method_to_return_type(self, data_type):
       element = []
       for garden in self.__gardens_list_objects:
           element.append({key: value for key, value in garden.__dict__.items()})
       return element

    def area_count_max(self, area_max: int):
        """Lambda need to search max area in garden manager"""
        result_str = ""

        result = [garden for garden in self.__gardens_list_objects if garden._garden_area < area_max]

        for garden in result:
            result_str += str(garden)

        return result_str

    def checker(self, condition):
        result = {
            "all": all(condition(garden) for garden in self.__gardens_list_objects),
            "any": any(condition(garden) for garden in self.__gardens_list_objects)
        }
        return result

    def flower_count_max(self, flower_max: int):
        """Lambda need to search max flower in garden manager"""
        result_str = ""

        result = [garden for garden in self.__gardens_list_objects if garden._garden_area < flower_max]

        for garden in result:
            result_str += str(garden)

        return result_str

    def enumerate(self):
        result = ""
        index = 1
        for garden in self.__gardens_list_objects:
            result += str(index) + ". " + str(garden) + "\n"
            index += 1
        return result

    def __len__(self):
        return len(self.__gardens_list_objects)

    def __getitem__(self, index):
        return self.__gardens_list_objects[index] if index <= len(self.__gardens_list_objects) else None

    def __iter__(self):
        return iter(self.__gardens_list_objects)

    def __str__(self):
        result = ""
        for garden in self.__gardens_list_objects:
            result += garden.__str__()
        return result + "\n"
