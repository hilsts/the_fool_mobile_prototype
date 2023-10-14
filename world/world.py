import data.data_handler as data_handler

WORLDS_PATH = "../data/world/worlds.json"
WORLD_PATH = "../data/world/world.json"


class World():

    def __init__(self, world_id=None):

        self.world_id = world_id

    def create_world(self):
        print('CRIANDO MUNDO AQUI')
        if data_handler.verify_path_exists(WORLDS_PATH):

            worlds = data_handler.get_file_data(WORLDS_PATH)
            world = data_handler.get_file_data(WORLD_PATH)
            self.world_id = worlds[-1]+1


            worlds.append(self.world_id)
            world.append({})

            data_handler.create_file_from_data(worlds, WORLDS_PATH)
            data_handler.create_file_from_data(world, WORLD_PATH)

        else:
            self.world_id = 0
            worlds = [self.world_id]
            data_handler.create_file_from_data(worlds, WORLDS_PATH)

            world = [{}]
            data_handler.create_file_from_data(world, WORLD_PATH)

    def list_worlds(self):

        worlds = data_handler.get_file_data(WORLDS_PATH)

    def build_world(self, class_id):

        from static.classes import CLASSES_EDGES, CLASSES

        class_name = CLASSES[class_id]

        mechanics = [class_name]
        for ce in CLASSES_EDGES:
            if class_name in ce:
                for mechanic in list(ce):
                    if mechanic != class_name:
                        mechanics.append(mechanic)

        return mechanics






