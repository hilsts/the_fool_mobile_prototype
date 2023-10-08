

MECHANIC_PATH = "../data/mechanic/mechanic.json"

class Mechanic():

    def __init__(self):

        self.zero = 0

    def build_mechanic(self, start):


        self.level = start['level']
        self.level_per_day = start['level_per_hour']
        self.quant_per_level = start["quant_per_level"]
        self.resource_class = start["resource_class"]
        self.resource_class_per_level = start["resource_class_per_level"]

        print(self.__dict__)
# Mechanic = type('Mechanic', (object,), {
#     "level" : 1,
#     "level_per_hour" : 5,
#     "quant_per_level" : 0.1,
#     "resource_class" : 1,
#     "resource_class_per_level" : 0.01
# })
#
# mec = Mechanic()
# print(mec.level)