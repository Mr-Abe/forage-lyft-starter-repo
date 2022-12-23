from datetime import date
from engine.Car import Car


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car("Calliope", "Model X", current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car("Glissade", "Model Y", current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        return Car("Palindrome", "Model Z", current_date, last_service_date, warning_light_on=warning_light_on)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car("Rorschach", "Model A", current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        return Car("Thovex", "Model B", current_date, last_service_date, current_mileage, last_service_mileage)