from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date: str) -> None:
        """
        Initialize the class.

        Args:
            last_service_date: The date of the last service.
        """
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self, car: Car) -> bool:
        """
        Check if the car needs service.

        :param car: The car to check.
        :return: True if the car needs service, False otherwise.
        """
        return