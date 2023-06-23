from managers.garden_manager import GardenManager


class SetManager:
    def __init__(self, garden_manager_list: GardenManager = None):
        self._garden_list_object = garden_manager_list

    def __iter__(self):
        return self._garden_list_object.__iter__()

    def __len__(self):
        result = 0
        for garden in self._garden_list_object:
            result += len(garden.__iter__())
        return result


