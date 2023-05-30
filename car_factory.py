from engine.capulet_engine import CapuletEngine
from engine.willough_by_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.octoprime_tire import OctoprimeTires
from tire.carrigan_tire import CarriganTires
from car import Car

class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, last_service_mileage, current_milage):
        return Car(CapuletEngine(last_service_mileage=last_service_mileage,current_milage=current_milage), SpindlerBattery(last_service_date, current_date), OctoprimeTires([0.1,0.1,0.1,0.1]))
    
    @staticmethod
    def create_glissade(current_date, last_service_date, last_service_mileage, current_milage):
        return Car(WilloughbyEngine(last_service_mileage=last_service_mileage,current_milage=current_milage), SpindlerBattery(last_service_date, current_date), OctoprimeTires([0.1,0.8,0.1,0.9]))
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on):
        return Car(SternmanEngine(warning_light_on=warning_light_on),SpindlerBattery(last_service_date, current_date), CarriganTires([0.5,0.6,0.8,0.4]))
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, last_service_mileage, current_milage):
        return Car(WilloughbyEngine(last_service_mileage=last_service_mileage,current_milage=current_milage), NubbinBattery(last_service_date, current_date), CarriganTires([0.5,0.6,0.8,0.4]))
    
    @staticmethod
    def create_thovex(current_date, last_service_date, last_service_mileage, current_milage):
        return Car(CapuletEngine(last_service_mileage=last_service_mileage,current_milage=current_milage), NubbinBattery(last_service_date, current_date), CarriganTires([0.5,0.6,0.8,0.4]))
    