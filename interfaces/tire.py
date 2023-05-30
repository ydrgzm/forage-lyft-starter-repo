from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, tires_list:list):
        self.tires_list = tires_list
        
    @abstractmethod
    def needs_service(self):
        pass