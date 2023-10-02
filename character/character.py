from static.classes import CLASSES_EDGES, CLASSES


class Character():

    def __init__(self, class_id, name):

        self.name = name
        self.class_ = CLASSES[class_id]
