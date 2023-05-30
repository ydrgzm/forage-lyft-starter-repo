# from abc import abstractmethod
from interfaces.serviceable import Serviceable
from interfaces.battery import Battery
from interfaces.engine import Engine
from interfaces.tire import Tire

class Car(Serviceable):
    def __init__(self, engine:Engine, battery:Battery, tires:Tire):
        self.engine = engine
        self.battery = battery
        self.tires = tires
    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()