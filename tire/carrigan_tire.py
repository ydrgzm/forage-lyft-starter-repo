from interfaces.tire import Tire

class CarriganTires(Tire):
    def __init__(self, tires_list:list):
        self.tires_list = tires_list

    def needs_service(self):
        for tire in self.tires_list:
            if tire >=0.9:
                return True
        return False