from engine.capulet_engine import CapuletEngine
from engine.willough_by_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from car import Car

class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, last_service_mileage, current_milage):
        return Car(CapuletEngine(last_service_mileage=last_service_mileage,current_milage=current_milage), SpindlerBattery(last_service_date, current_date))
    
    @staticmethod
    def create_glissade(current_date, last_service_date, last_service_mileage, current_milage):
        return Car(WilloughbyEngine(last_service_mileage=last_service_mileage,current_milage=current_milage), SpindlerBattery(last_service_date, current_date))
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on=warning_light_on),SpindlerBattery(last_service_date, current_date))
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, last_service_mileage, current_milage):
        return Car(WilloughbyEngine(last_service_mileage=last_service_mileage,current_milage=current_milage), NubbinBattery(last_service_date, current_date))
    
    @staticmethod
    def create_thovex(current_date, last_service_date, last_service_mileage, current_milage):
        return Car(CapuletEngine(last_service_mileage=last_service_mileage,current_milage=current_milage), NubbinBattery(last_service_date, current_date))
    