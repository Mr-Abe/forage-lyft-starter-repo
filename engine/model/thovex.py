from datetime import datetime

from engine.CapuletEngine import CapuletEngine


class Thovex(CapuletEngine):
    def needs_service(self) -> bool:
        """
        Returns True if the car needs service, False otherwise.
        """
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False