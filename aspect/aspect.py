from data import data_handler
from world.world import World
MECHANIC_PATH = "../data/mechanic/mechanic.json"

ASPECTS = ["time", "nature", "politics", "economy", "relatioship"]


class Aspect(World):

    def __init__(self):

        super().__init__()


    def build_aspects(self, start):


        print(self.__dict__)