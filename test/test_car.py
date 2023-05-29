import unittest
from datetime import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willough_by_engine import WilloughbyEngine

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        car = NubbinBattery(last_service_date, today)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = NubbinBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        car = SpindlerBattery(last_service_date, today)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        car = SpindlerBattery(last_service_date, today)
        self.assertFalse(car.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 0

        car = CapuletEngine(last_service_mileage,current_mileage)
        self.assertTrue(car.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 100000

        car = CapuletEngine(last_service_mileage,current_mileage )
        self.assertFalse(car.needs_service())

class TestWilloughByEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 0

        car = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertTrue(car.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        current_mileage = 100000
        last_service_mileage = 100000

        car = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertFalse(car.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        car = SternmanEngine(True)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = SternmanEngine(False)
        self.assertTrue(car.needs_service())

    
if __name__ == '__main__':
    unittest.main()
