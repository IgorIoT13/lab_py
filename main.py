from model.botanic_garden import Botanic_garden
from model.university_garden import University_garden
from managers.garden_manager import Garden_manager

garden = Garden_manager()

garden.add_to_garden(Botanic_garden(1, 2, 1))
garden.add_to_garden(University_garden(1, 2, 4))

print(garden.get_greenhouse_count_max(2))
print(garden.get_sculpture_count_max(2))


print(garden.__str__())
