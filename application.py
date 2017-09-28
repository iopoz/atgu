from models.general_model import GeneralModel


class Application(object):
    def __init__(self):
        pass

    @property
    def general(self): return GeneralModel(self)