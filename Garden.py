class Garden:
    def __init__(self, area: int, orchard: bool, vegetable_garden: bool, flower: int):
        self.__private_area = area if area is not None else 0
        self.__private_has_orchard = orchard if orchard is not None else False
        self.__private_has_vegetable_garden = vegetable_garden if vegetable_garden is not None else False
        self.__private_number_of_flower = flower if flower is not None else 0

    def public_plant_flower(self, count):
        if count >= 0:
            self.__private_number_of_flower += count

    def public_remove_flower(self, count):
        if count >= 0:
            self.__private_number_of_flower -= count

    def public_add_vegetable_region (self, count):
       if count >= 0 :
           self.__private_area += count

    def public_print_all_stats_object(self):
        print("area :", self.__private_area,
              ", orchard :", self.__private_has_orchard,
              ", vegetable garden :", self.__private_has_vegetable_garden,
              ", flower :", self.__private_number_of_flower)