from battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, last_service_date:int, current_date:int):
        self.last_service_date = last_service_date
        self.current_date = current_date    

    def needs_service(self):
        # return difference of year is greater than 2
        return self.current_date - self.last_service_date > 2