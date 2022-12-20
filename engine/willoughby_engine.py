from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date: str, current_mileage: int, last_service_mileage: int):
        """
        Initialize the class

        :param last_service_date: The date of the last service
        :param current_mileage: The current mileage of the car
        :param last_service_mileage: The mileage of the car at the last service
        """
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self) -> bool:
        """
        Check if the engine should be serviced.

        :return: True if the engine should be serviced, False otherwise.
        """
        return self.current_mileage - self.last_service_mileage > 60000