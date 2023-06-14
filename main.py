from model.botanic_garden import BotanicGarden
from model.university_garden import UniversityGarden
from managers.garden_manager import GardenManager

garden = GardenManager()

garden.add_to_garden(BotanicGarden(2, 1, 0))

garden.add_to_garden(BotanicGarden(3, 2, 1))
garden.add_to_garden(BotanicGarden(2, 3, 0))
garden.add_to_garden(BotanicGarden(1, 4, 1))


garden.add_to_garden(UniversityGarden(10, 20, 40))


print(garden.area_count_max(5))

print(garden.flower_count_max(5))

print(garden.enumerate())

print(garden.zip())

print(garden.method_to_return_type(int))

result = garden.checker(lambda garden: garden._garden_area < 100)
print(result)
