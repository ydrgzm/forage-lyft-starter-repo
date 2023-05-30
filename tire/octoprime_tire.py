from interfaces.tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, tires_list:list):
        self.tires_list = tires_list

    def needs_service(self):
        val = sum(self.tires_list)
        if val >= 3:
            return True
        return False