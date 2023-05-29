# from abc import abstractmethod
from engine.interfaces.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery
