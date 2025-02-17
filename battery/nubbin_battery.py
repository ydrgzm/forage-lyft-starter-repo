from battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date:int, current_date:int):
        self.last_service_date = last_service_date
        self.current_date = current_date    
        
    def needs_service(self):
        # return difference of year is greater than 2
        return self.current_date.year - self.last_service_date.year > 4