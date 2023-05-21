from model.garden import Garden
from model.botanic_garden import Botanic_garden
from model.university_garden import University_garden

class Garden_manager:
    def __init__(self):
        self.__gardens_list_objects = []

    def add_to_garden(self, obj_garden: Garden):
        self.__gardens_list_objects.append(obj_garden)

    def __str__(self):
        result = ""
        for garden in self.__gardens_list_objects:
            result += garden.__str__()
        return result + "\n"

    def get_sculpture_count_max(self, max_sculpture):
        result = ""
        for garden in self.__gardens_list_objects:
            current_obj: Garden = lambda garden : garden < max_sculpture
            result += current_obj.__str__()
        return result + "\n"

    def get_greenhouse_count_max(self, max_greenhouse):
        result = ""
        for garden in self.__gardens_list_objects:
            if isinstance(garden, Botanic_garden):
                current_obj = lambda garden: garden.get_count_greenhouses() < max_greenhouse
                result += current_obj.__str__()
        return result + "\n"
