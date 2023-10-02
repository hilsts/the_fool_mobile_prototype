import data.data_handler as data_handler

WORLDS_PATH = "../data/world/worlds.json"
WORLD_PATH = "../data/world/world.json"


class World():

    def __init__(self, world_id=None):

        self.world_id = self.start_world(world_id)


    def start_world(self, world_id):

        if world_id is None:

            return self.create_world()

        else:

            world_data = data_handler.get_file_data(WORLD_PATH)[world_id]



    def create_world(self):

        if data_handler.verify_path_exists(WORLDS_PATH):

            worlds = data_handler.get_file_data(WORLDS_PATH)
            world = data_handler.get_file_data(WORLD_PATH)

            worlds.append(worlds[-1]+1)
            world.append({})

            data_handler.create_file_from_data(worlds, WORLDS_PATH)
            data_handler.create_file_from_data(world, WORLD_PATH)

        else:

            worlds = [0]
            data_handler.create_file_from_data(worlds, WORLDS_PATH)

            world = [{}]
            data_handler.create_file_from_data(world, WORLD_PATH)