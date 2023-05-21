import Garden

garden = Garden.Garden(1 , True, False, 10)

garden.public_print_all_stats_object()

garden.public_plant_flower(15)
garden.public_add_vegetable_region(10)
garden.public_remove_flower(3)

garden.public_print_all_stats_object()