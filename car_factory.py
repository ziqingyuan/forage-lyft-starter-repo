from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(capulet_engine, spindler_battery)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(willoughby_engine, spindler_battery)

    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        sternman_engine = SternmanEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(sternman_engine, spindler_battery)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Car(willoughby_engine, nubbin_battery)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Car(capulet_engine, nubbin_battery)